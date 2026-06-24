$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
$skillsRoot = Join-Path $repoRoot "skills"

Get-ChildItem -LiteralPath $skillsRoot -Filter "SKILL.md" -Recurse -File |
  Sort-Object FullName |
  ForEach-Object {
    $_.FullName.Substring($repoRoot.Length + 1).Replace("\", "/")
  }
