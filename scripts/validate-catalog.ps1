$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
$skillsRoot = Join-Path $repoRoot "skills"
$errors = New-Object System.Collections.Generic.List[string]

function Get-RelativePath([string]$path) {
  return $path.Substring($repoRoot.Length + 1).Replace("\", "/")
}

function Read-Text([string]$path) {
  return [System.IO.File]::ReadAllText($path)
}

function Get-Frontmatter([string]$skillPath) {
  $content = Read-Text $skillPath
  $match = [regex]::Match($content, "(?s)\A---\s*(.*?)\s*---")
  if (-not $match.Success) {
    return $null
  }
  return $match.Groups[1].Value
}

function Get-FrontmatterName([string]$skillPath) {
  $frontmatter = Get-Frontmatter $skillPath
  if ($null -eq $frontmatter) {
    return $null
  }
  $nameMatch = [regex]::Match($frontmatter, "(?m)^name:\s*([a-z0-9][a-z0-9-]*[a-z0-9]|[a-z0-9])\s*$")
  if (-not $nameMatch.Success) {
    return $null
  }
  return $nameMatch.Groups[1].Value
}

function Get-FrontmatterDescription([string]$skillPath) {
  $frontmatter = Get-Frontmatter $skillPath
  if ($null -eq $frontmatter) {
    return $null
  }

  $lines = $frontmatter -split "\r?\n"
  for ($index = 0; $index -lt $lines.Count; $index++) {
    if ($lines[$index] -notmatch "^description:\s*(.*)$") {
      continue
    }

    $value = $Matches[1].Trim()
    if ($value -notmatch "^[>|][+-]?$") {
      return $value.Trim('"').Trim("'")
    }

    $separator = if ($value.StartsWith("|")) { "`n" } else { " " }
    $parts = New-Object System.Collections.Generic.List[string]
    for ($lineIndex = $index + 1; $lineIndex -lt $lines.Count; $lineIndex++) {
      $line = $lines[$lineIndex]
      if ($line -match "^\s+(.*)$") {
        $parts.Add($Matches[1].Trim()) | Out-Null
      } elseif ([string]::IsNullOrWhiteSpace($line)) {
        $parts.Add("") | Out-Null
      } else {
        break
      }
    }
    return [string]::Join($separator, $parts).Trim()
  }

  return $null
}

function Add-Error([string]$message) {
  $errors.Add($message) | Out-Null
}

$rootReadmePath = Join-Path $repoRoot "README.md"
$rootManifestPath = Join-Path $repoRoot ".claude-plugin\plugin.json"
$skillsShPath = Join-Path $repoRoot "skills.sh.json"

foreach ($requiredPath in @($rootReadmePath, $rootManifestPath, $skillsShPath)) {
  if (-not (Test-Path -LiteralPath $requiredPath)) {
    Add-Error "Missing required catalog file: $(Get-RelativePath $requiredPath)"
  }
}

if ($errors.Count -gt 0) {
  $errors | ForEach-Object { Write-Error $_ }
  exit 1
}

$rootReadme = Read-Text $rootReadmePath
$rootManifest = Get-Content -LiteralPath $rootManifestPath -Raw | ConvertFrom-Json
$rootManifestSkills = @($rootManifest.skills)
$skillsSh = Get-Content -LiteralPath $skillsShPath -Raw | ConvertFrom-Json
$skillsShNames = @()
foreach ($group in @($skillsSh.groupings)) {
  $skillsShNames += @($group.skills)
}

$skillFiles = Get-ChildItem -LiteralPath $skillsRoot -Filter "SKILL.md" -Recurse -File |
  Sort-Object FullName

foreach ($skillFile in $skillFiles) {
  $skillDir = $skillFile.Directory
  $skillName = $skillDir.Name
  $categoryDir = $skillDir.Parent
  $categoryName = $categoryDir.Name
  $relativeSkillDir = Get-RelativePath $skillDir.FullName
  $manifestPath = "./$relativeSkillDir"
  $installCommand = "npx skills@latest add manansuneja/skills --skill $skillName -g"

  if ($relativeSkillDir -notmatch "^skills/[^/]+/[^/]+$") {
    Add-Error "$relativeSkillDir must follow skills/<category>/<skill-name>."
  }

  $frontmatterName = Get-FrontmatterName $skillFile.FullName
  if ($frontmatterName -ne $skillName) {
    Add-Error "$relativeSkillDir/SKILL.md frontmatter name must be '$skillName'."
  }

  $frontmatterDescription = Get-FrontmatterDescription $skillFile.FullName
  if ([string]::IsNullOrWhiteSpace($frontmatterDescription)) {
    Add-Error "$relativeSkillDir/SKILL.md frontmatter description must be non-empty."
  } elseif ($frontmatterDescription.Length -gt 1024) {
    Add-Error "$relativeSkillDir/SKILL.md frontmatter description exceeds 1,024 characters ($($frontmatterDescription.Length))."
  }

  if ($rootManifestSkills -notcontains $manifestPath) {
    Add-Error ".claude-plugin/plugin.json is missing $manifestPath."
  }

  if ($skillsShNames -notcontains $skillName) {
    Add-Error "skills.sh.json is missing skill '$skillName'."
  }

  if ($rootReadme -notlike "*$relativeSkillDir*") {
    Add-Error "README.md is missing path '$relativeSkillDir'."
  }

  if ($rootReadme -notlike "*$installCommand*") {
    Add-Error "README.md is missing install command '$installCommand'."
  }

  $categoryReadmePath = Join-Path $categoryDir.FullName "README.md"
  if (-not (Test-Path -LiteralPath $categoryReadmePath)) {
    Add-Error "Missing category README: skills/$categoryName/README.md."
  } else {
    $categoryReadme = Read-Text $categoryReadmePath
    if ($categoryReadme -notlike "*$skillName*") {
      Add-Error "skills/$categoryName/README.md is missing skill '$skillName'."
    }
    if ($categoryReadme -notlike "*$installCommand*") {
      Add-Error "skills/$categoryName/README.md is missing install command '$installCommand'."
    }
  }

  $skillReadmePath = Join-Path $skillDir.FullName "README.md"
  if (-not (Test-Path -LiteralPath $skillReadmePath)) {
    Add-Error "$relativeSkillDir is missing README.md."
  } else {
    $skillReadme = Read-Text $skillReadmePath
    if ($skillReadme -notlike "*$installCommand*") {
      Add-Error "$relativeSkillDir/README.md is missing install command '$installCommand'."
    }
    if ($skillReadme -notlike "*## What This Skill Does And How To Use It*") {
      Add-Error "$relativeSkillDir/README.md is missing bottom section 'What This Skill Does And How To Use It'."
    }
  }

  $skillManifestPath = Join-Path $skillDir.FullName ".claude-plugin\plugin.json"
  if (-not (Test-Path -LiteralPath $skillManifestPath)) {
    Add-Error "$relativeSkillDir is missing .claude-plugin/plugin.json."
  } else {
    $skillManifest = Get-Content -LiteralPath $skillManifestPath -Raw | ConvertFrom-Json
    if ($skillManifest.name -ne $skillName) {
      Add-Error "$relativeSkillDir/.claude-plugin/plugin.json name must be '$skillName'."
    }
    if ($skillManifest.repository -ne "https://github.com/manansuneja/skills") {
      Add-Error "$relativeSkillDir/.claude-plugin/plugin.json repository must be https://github.com/manansuneja/skills."
    }
  }
}

if ($errors.Count -gt 0) {
  $errors | ForEach-Object { Write-Error $_ }
  exit 1
}

Write-Host "Catalog validation passed for $($skillFiles.Count) skills."
