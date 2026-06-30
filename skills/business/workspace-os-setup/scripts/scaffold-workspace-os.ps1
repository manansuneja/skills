param(
    [Alias("BusinessName", "ProjectName")]
    [string] $WorkspaceName = "",
    [string] $TargetPath = ".",
    [ValidateSet("hub", "workspace", "workspace-hub", "business", "business-hub", "project", "client-project", "client-workspace", "client")]
    [string] $WorkspaceKind = "hub",
    [Alias("BusinessCategory")]
    [string] $WorkspaceCategory = "",
    [string] $Objective = "",
    [string] $PrimaryUse = "",
    [switch] $UseCurrentFolder,
    [switch] $CreateFolder
)

$ErrorActionPreference = "Stop"

function Get-Slug {
    param([string] $Value)

    if ([string]::IsNullOrWhiteSpace($Value)) {
        return "workspace-os"
    }

    $slug = $Value.ToLowerInvariant() -replace "[^a-z0-9]+", "-"
    $slug = $slug.Trim("-")

    if ([string]::IsNullOrWhiteSpace($slug)) {
        return "workspace-os"
    }

    return $slug
}

function Normalize-WorkspaceKind {
    param([string] $Value)

    $normalized = ($Value.ToLowerInvariant() -replace "[^a-z0-9]+", "-").Trim("-")
    switch ($normalized) {
        { $_ -in @("project", "client-project", "client", "client-workspace") } { return "project" }
        { $_ -in @("hub", "workspace", "workspace-hub", "business", "business-hub", "") } { return "hub" }
        default { throw "Unknown workspace kind: $Value. Use hub or project." }
    }
}

function Get-DocsRoot {
    param([string] $Kind)

    if ($Kind -eq "project") {
        return "project-docs"
    }

    return "workspace-hub-docs"
}

function Get-RelativePath {
    param(
        [string] $BasePath,
        [string] $Path
    )

    $base = [System.IO.Path]::GetFullPath($BasePath)
    $target = [System.IO.Path]::GetFullPath($Path)

    if ((Get-Item $base).PSIsContainer -and -not $base.EndsWith([System.IO.Path]::DirectorySeparatorChar)) {
        $base += [System.IO.Path]::DirectorySeparatorChar
    }

    $baseUri = New-Object System.Uri($base)
    $targetUri = New-Object System.Uri($target)
    return [Uri]::UnescapeDataString($baseUri.MakeRelativeUri($targetUri).ToString()).Replace("\", "/")
}

function Test-BroadFolder {
    param([System.IO.DirectoryInfo] $Directory)

    $broadNames = @(
        "desktop",
        "documents",
        "downloads",
        "repos",
        "repositories",
        "projects",
        "code",
        "dev",
        "source",
        "workspace",
        "workspaces"
    )

    $name = $Directory.Name.ToLowerInvariant()
    if ($broadNames -contains $name) {
        return $true
    }

    $root = [System.IO.Path]::GetPathRoot($Directory.FullName)
    if ($Directory.FullName.TrimEnd("\", "/") -eq $root.TrimEnd("\", "/")) {
        return $true
    }

    $topLevelCount = @(Get-ChildItem -LiteralPath $Directory.FullName -Force).Count
    return $topLevelCount -gt 8
}

function Test-NearlyEmptyFolder {
    param([System.IO.DirectoryInfo] $Directory)

    $items = @(Get-ChildItem -LiteralPath $Directory.FullName -Force)
    return $items.Count -le 1
}

function Resolve-WorkspaceRoot {
    param(
        [string] $BasePath,
        [string] $Name,
        [switch] $UseCurrent,
        [switch] $CreateNew
    )

    $base = Resolve-Path -LiteralPath $BasePath
    $baseItem = Get-Item -LiteralPath $base
    if (-not $baseItem.PSIsContainer) {
        throw "TargetPath must be a folder: $BasePath"
    }

    $slug = Get-Slug $Name
    if ($CreateNew) {
        return Join-Path $baseItem.FullName "$slug-workspace"
    }

    if ($UseCurrent) {
        return $baseItem.FullName
    }

    $leaf = $baseItem.Name.ToLowerInvariant()
    if ((Test-NearlyEmptyFolder $baseItem) -or $leaf.Contains($slug)) {
        return $baseItem.FullName
    }

    if (Test-BroadFolder $baseItem) {
        return Join-Path $baseItem.FullName "$slug-workspace"
    }

    throw "Target folder is not empty. Re-run with -UseCurrentFolder to add the Workspace OS here, or -CreateFolder to create a new workspace folder."
}

function Assert-NoExistingWorkspaceOs {
    param([string] $WorkspaceRoot)

    if (-not (Test-Path -LiteralPath $WorkspaceRoot -PathType Container)) {
        return
    }

    $workspaceOsMarkers = @("AGENTS.md", "INDEX.md", "agents", "_workspace_setup_docs", "workspace-best-practices", "workspace-hub-docs", "project-docs", "workspace-skills", "business-skills", "business-practices", "business-hub-docs")
    foreach ($marker in $workspaceOsMarkers) {
        if (Test-Path -LiteralPath (Join-Path $WorkspaceRoot $marker)) {
            throw "The target already looks like a Workspace OS workspace: $WorkspaceRoot"
        }
    }
}

function Assert-SafeWorkspaceRoot {
    param(
        [string] $WorkspaceRoot,
        [string] $BaseRoot
    )

    Assert-NoExistingWorkspaceOs -WorkspaceRoot $WorkspaceRoot

    $normalizedWorkspaceRoot = [System.IO.Path]::GetFullPath($WorkspaceRoot).TrimEnd("\", "/")
    $normalizedBaseRoot = [System.IO.Path]::GetFullPath($BaseRoot).TrimEnd("\", "/")
    if (
        $normalizedWorkspaceRoot -ne $normalizedBaseRoot -and
        (Test-Path -LiteralPath $WorkspaceRoot -PathType Container) -and
        @(Get-ChildItem -LiteralPath $WorkspaceRoot -Force).Count -gt 0
    ) {
        throw "Refusing to merge into an existing non-empty workspace folder: $WorkspaceRoot"
    }
}

function Copy-TemplateContents {
    param(
        [string] $TemplateRoot,
        [string] $WorkspaceRoot,
        [string] $Name,
        [string] $Kind,
        [string] $Category,
        [string] $Goal,
        [string] $UseCase
    )

    $docsRoot = Get-DocsRoot $Kind

    $templateFiles = Get-ChildItem -LiteralPath $TemplateRoot -Recurse -File -Force
    $copyPlan = @()
    foreach ($file in $templateFiles) {
        $relative = Get-RelativePath $TemplateRoot $file.FullName
        if ($relative.StartsWith("workspace-hub-docs/")) {
            $relative = "$docsRoot/" + $relative.Substring("workspace-hub-docs/".Length)
        }
        $destination = Join-Path $WorkspaceRoot ($relative.Replace("/", "\"))

        if (Test-Path -LiteralPath $destination) {
            throw "Refusing to overwrite existing file: $destination"
        }

        $copyPlan += [PSCustomObject]@{
            Source = $file
            Destination = $destination
        }
    }

    # Do not write until every mapped destination has passed the collision check.
    New-Item -ItemType Directory -Force -Path $WorkspaceRoot | Out-Null
    $utf8NoBom = [System.Text.UTF8Encoding]::new($false)
    foreach ($item in $copyPlan) {
        $file = $item.Source
        $destination = $item.Destination

        $destinationDirectory = Split-Path -Parent $destination
        New-Item -ItemType Directory -Force -Path $destinationDirectory | Out-Null
        Copy-Item -LiteralPath $file.FullName -Destination $destination

        $isTemplateText = $file.Extension -in @(".md", ".mdc", ".txt", ".json")
        if ($isTemplateText) {
            $content = Get-Content -LiteralPath $destination -Raw
            if (-not [string]::IsNullOrWhiteSpace($Name)) {
                $content = $content.Replace("{{WORKSPACE_NAME}}", $Name)
                $content = $content.Replace("{{BUSINESS_NAME}}", $Name)
                $content = $content.Replace("{{PROJECT_NAME}}", $Name)
            }
            if (-not [string]::IsNullOrWhiteSpace($Category)) {
                $content = $content.Replace("{{WORKSPACE_CATEGORY}}", $Category)
                $content = $content.Replace("{{BUSINESS_CATEGORY}}", $Category)
            }
            if (-not [string]::IsNullOrWhiteSpace($Goal)) {
                $content = $content.Replace("{{OBJECTIVE}}", $Goal)
            }
            if (-not [string]::IsNullOrWhiteSpace($UseCase)) {
                $content = $content.Replace("{{PRIMARY_USE}}", $UseCase)
            }
            $content = $content.Replace("{{DOCS_ROOT}}", $docsRoot)
            $content = $content.Replace("{{WORKSPACE_KIND}}", $Kind)
            $content = $content.Replace("{{DATE}}", (Get-Date -Format "MMM-dd-yyyy"))
            [System.IO.File]::WriteAllText($destination, $content, $utf8NoBom)
        }
    }
}

$skillRoot = Split-Path -Parent $PSScriptRoot
$templateRoot = Join-Path $skillRoot "assets\workspace-os-workspace"
if (-not (Test-Path -LiteralPath $templateRoot -PathType Container)) {
    throw "Missing template folder: $templateRoot"
}

if ($UseCurrentFolder -and $CreateFolder) {
    throw "Choose either -UseCurrentFolder or -CreateFolder, not both."
}

if ([string]::IsNullOrWhiteSpace($WorkspaceName)) {
    throw "-WorkspaceName is required (-BusinessName and -ProjectName are aliases)."
}

$WorkspaceKind = Normalize-WorkspaceKind $WorkspaceKind
$workspaceRoot = Resolve-WorkspaceRoot -BasePath $TargetPath -Name $WorkspaceName -UseCurrent:$UseCurrentFolder -CreateNew:$CreateFolder
$baseRoot = (Resolve-Path -LiteralPath $TargetPath).Path
Assert-SafeWorkspaceRoot -WorkspaceRoot $workspaceRoot -BaseRoot $baseRoot
Copy-TemplateContents -TemplateRoot $templateRoot -WorkspaceRoot $workspaceRoot -Name $WorkspaceName -Kind $WorkspaceKind -Category $WorkspaceCategory -Goal $Objective -UseCase $PrimaryUse

Write-Output "Workspace OS workspace created: $workspaceRoot"
Write-Output "Open START_HERE.md first. Your primary workspace is $(Join-Path $workspaceRoot (Get-DocsRoot $WorkspaceKind))."
Write-Output "Use workspace-best-practices/ to customize skills, templates, and examples by asking your agent."
Write-Output "Agents manage AGENTS.md, agents/, and _workspace_setup_docs/ in the background."
Write-Output "To personalize later, tell your agent: Customize my workspace."
