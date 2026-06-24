param(
  [switch]$ForceReplace
)

$ErrorActionPreference = "Stop"

$repoRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
$skillsRoot = Join-Path $repoRoot "skills"
$agentRoots = @(
  (Join-Path $HOME ".claude\skills"),
  (Join-Path $HOME ".agents\skills")
)

$publicSkills = Get-ChildItem -LiteralPath $skillsRoot -Filter "SKILL.md" -Recurse -File |
  Sort-Object FullName |
  ForEach-Object { $_.Directory }

foreach ($agentRoot in $agentRoots) {
  New-Item -ItemType Directory -Force -Path $agentRoot | Out-Null

  foreach ($skillDir in $publicSkills) {
    $name = $skillDir.Name
    $destination = Join-Path $agentRoot $name

    if (Test-Path -LiteralPath $destination) {
      $existing = Get-Item -LiteralPath $destination -Force
      $isReparsePoint = (($existing.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0)

      if ($isReparsePoint) {
        Remove-Item -LiteralPath $destination -Force
      } elseif ($ForceReplace) {
        $stamp = Get-Date -Format "yyyyMMdd-HHmmss"
        $backup = "$destination.backup-$stamp"
        Move-Item -LiteralPath $destination -Destination $backup
        Write-Host "Backed up existing $destination to $backup"
      } else {
        Write-Warning "Skipping existing non-junction path: $destination. Re-run with -ForceReplace to back it up and replace it."
        continue
      }
    }

    New-Item -ItemType Junction -Path $destination -Target $skillDir.FullName | Out-Null
    Write-Host "Linked $destination -> $($skillDir.FullName)"
  }
}
