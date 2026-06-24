param(
    [string] $ProjectName = "",
    [string] $TargetPath = ".",
    [switch] $UseCurrentFolder,
    [switch] $CreateFolder
)

$ErrorActionPreference = "Stop"

function Get-Slug {
    param([string] $Value)

    if ([string]::IsNullOrWhiteSpace($Value)) {
        return "pm-os"
    }

    $slug = $Value.ToLowerInvariant() -replace "[^a-z0-9]+", "-"
    $slug = $slug.Trim("-")

    if ([string]::IsNullOrWhiteSpace($slug)) {
        return "pm-os"
    }

    return $slug
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

    throw "Target folder is not empty. Re-run with -UseCurrentFolder to add the PM OS here, or -CreateFolder to create a new workspace folder."
}

function Assert-NoExistingPmOs {
    param([string] $WorkspaceRoot)

    if (-not (Test-Path -LiteralPath $WorkspaceRoot -PathType Container)) {
        return
    }

    $pmOsMarkers = @("AGENTS.md", "INDEX.md", "agents", "skills", "product-docs")
    foreach ($marker in $pmOsMarkers) {
        if (Test-Path -LiteralPath (Join-Path $WorkspaceRoot $marker)) {
            throw "The target already looks like a PM OS workspace: $WorkspaceRoot"
        }
    }
}

function Copy-TemplateContents {
    param(
        [string] $TemplateRoot,
        [string] $WorkspaceRoot,
        [string] $Name
    )

    New-Item -ItemType Directory -Force -Path $WorkspaceRoot | Out-Null

    $templateFiles = Get-ChildItem -LiteralPath $TemplateRoot -Recurse -File -Force
    foreach ($file in $templateFiles) {
        $relative = Get-RelativePath $TemplateRoot $file.FullName
        $destination = Join-Path $WorkspaceRoot ($relative.Replace("/", "\"))

        if (Test-Path -LiteralPath $destination) {
            throw "Refusing to overwrite existing file: $destination"
        }

        $destinationDirectory = Split-Path -Parent $destination
        New-Item -ItemType Directory -Force -Path $destinationDirectory | Out-Null
        Copy-Item -LiteralPath $file.FullName -Destination $destination

        $isTemplateText = $file.Extension -in @(".md", ".mdc", ".txt", ".json")
        $isSetupFile = $relative -eq "_setup/README.md" -or $relative.StartsWith("_setup/")
        if ($isTemplateText -and -not $isSetupFile) {
            $content = Get-Content -LiteralPath $destination -Raw
            if (-not [string]::IsNullOrWhiteSpace($Name)) {
                $content = $content.Replace("{{PROJECT_NAME}}", $Name)
            }
            $content = $content.Replace("{{DATE}}", (Get-Date -Format "yyyy-MM-dd"))
            Set-Content -LiteralPath $destination -Value $content -NoNewline
        }
    }
}

$skillRoot = Split-Path -Parent $PSScriptRoot
$templateRoot = Join-Path $skillRoot "assets\pm-os-workspace"
if (-not (Test-Path -LiteralPath $templateRoot -PathType Container)) {
    throw "Missing template folder: $templateRoot"
}

if ($UseCurrentFolder -and $CreateFolder) {
    throw "Choose either -UseCurrentFolder or -CreateFolder, not both."
}

$workspaceRoot = Resolve-WorkspaceRoot -BasePath $TargetPath -Name $ProjectName -UseCurrent:$UseCurrentFolder -CreateNew:$CreateFolder
Assert-NoExistingPmOs -WorkspaceRoot $workspaceRoot
Copy-TemplateContents -TemplateRoot $templateRoot -WorkspaceRoot $workspaceRoot -Name $ProjectName

Write-Output "PM OS workspace created: $workspaceRoot"
Write-Output "Open INDEX.md first, then README.md, AGENTS.md, and _setup/README.md."
