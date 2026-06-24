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

function Get-FrontmatterName([string]$skillPath) {
  $content = Read-Text $skillPath
  $match = [regex]::Match($content, "(?s)\A---\s*(.*?)\s*---")
  if (-not $match.Success) {
    return $null
  }
  $nameMatch = [regex]::Match($match.Groups[1].Value, "(?m)^name:\s*([a-z0-9][a-z0-9-]*[a-z0-9]|[a-z0-9])\s*$")
  if (-not $nameMatch.Success) {
    return $null
  }
  return $nameMatch.Groups[1].Value
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
