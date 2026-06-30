#!/usr/bin/env bash
set -euo pipefail

project_name=""
target_path="."
use_current_folder=false
create_folder=false

usage() {
  cat <<'EOF'
Usage:
  scaffold-pm-os.sh --project-name "Product Name" --target-path "." --use-current-folder
  scaffold-pm-os.sh --project-name "Product Name" --target-path "." --create-folder
EOF
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --project-name)
      project_name="${2:-}"
      shift 2
      ;;
    --target-path)
      target_path="${2:-}"
      shift 2
      ;;
    --use-current-folder)
      use_current_folder=true
      shift
      ;;
    --create-folder)
      create_folder=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

if [ "$use_current_folder" = true ] && [ "$create_folder" = true ]; then
  echo "Choose either --use-current-folder or --create-folder, not both." >&2
  exit 1
fi

get_slug() {
  local value="$1"
  local slug

  if [ -z "${value//[[:space:]]/}" ]; then
    printf '%s\n' "pm-os"
    return
  fi

  slug="$(printf '%s' "$value" |
    tr '[:upper:]' '[:lower:]' |
    sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//')"

  if [ -z "$slug" ]; then
    printf '%s\n' "pm-os"
  else
    printf '%s\n' "$slug"
  fi
}

absolute_dir() {
  local path="$1"
  (cd "$path" && pwd -P)
}

is_broad_folder() {
  local dir="$1"
  local name
  name="$(basename "$dir" | tr '[:upper:]' '[:lower:]')"

  case "$name" in
    desktop|documents|downloads|repos|repositories|projects|code|dev|source|workspace|workspaces)
      return 0
      ;;
  esac

  if [ "$dir" = "/" ]; then
    return 0
  fi

  local count
  count="$(find "$dir" -mindepth 1 -maxdepth 1 -print | wc -l | tr -d '[:space:]')"
  [ "${count:-0}" -gt 8 ]
}

is_nearly_empty_folder() {
  local dir="$1"
  local count
  count="$(find "$dir" -mindepth 1 -maxdepth 1 -print | wc -l | tr -d '[:space:]')"
  [ "${count:-0}" -le 1 ]
}

resolve_workspace_root() {
  local base_path="$1"
  local name="$2"
  local base
  local leaf
  local slug

  if [ ! -d "$base_path" ]; then
    echo "TargetPath must be a folder: $base_path" >&2
    exit 1
  fi

  base="$(absolute_dir "$base_path")"
  slug="$(get_slug "$name")"

  if [ "$create_folder" = true ]; then
    printf '%s\n' "$base/$slug-workspace"
    return
  fi

  if [ "$use_current_folder" = true ]; then
    printf '%s\n' "$base"
    return
  fi

  leaf="$(basename "$base" | tr '[:upper:]' '[:lower:]')"
  if is_nearly_empty_folder "$base" || [[ "$leaf" == *"$slug"* ]]; then
    printf '%s\n' "$base"
    return
  fi

  if is_broad_folder "$base"; then
    printf '%s\n' "$base/$slug-workspace"
    return
  fi

  echo "Target folder is not empty. Re-run with --use-current-folder to add the PM OS here, or --create-folder to create a new workspace folder." >&2
  exit 1
}

assert_no_existing_pm_os() {
  local workspace_root="$1"
  local marker

  if [ ! -d "$workspace_root" ]; then
    return
  fi

  for marker in AGENTS.md INDEX.md agents _workspace_setup_docs product-skills product-docs; do
    if [ -e "$workspace_root/$marker" ]; then
      echo "The target already looks like a PM OS workspace: $workspace_root" >&2
      exit 1
    fi
  done
}

copy_template_contents() {
  local template_root="$1"
  local workspace_root="$2"
  local name="$3"
  local today
  today="$(LC_TIME=C date '+%b-%d-%Y')"

  mkdir -p "$workspace_root"

  while IFS= read -r -d '' file; do
    local relative
    local destination
    local destination_dir
    relative="${file#$template_root/}"
    destination="$workspace_root/$relative"
    destination_dir="$(dirname "$destination")"

    if [ -e "$destination" ]; then
      echo "Refusing to overwrite existing file: $destination" >&2
      exit 1
    fi

    mkdir -p "$destination_dir"
    cp "$file" "$destination"

    case "$relative" in
      _workspace_setup_docs/personalization/*)
        continue
        ;;
    esac

    case "$file" in
      *.md|*.mdc|*.txt|*.json)
        if [ -n "${name//[[:space:]]/}" ]; then
          PROJECT_NAME_VALUE="$name" perl -0pi -e 's/\{\{PROJECT_NAME\}\}/$ENV{PROJECT_NAME_VALUE}/g' "$destination"
        fi
        DATE_VALUE="$today" perl -0pi -e 's/\{\{DATE\}\}/$ENV{DATE_VALUE}/g' "$destination"
        ;;
    esac
  done < <(find "$template_root" -type f -print0)
}

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
skill_root="$(cd "$script_dir/.." && pwd -P)"
template_root="$skill_root/assets/pm-os-workspace"

if [ ! -d "$template_root" ]; then
  echo "Missing template folder: $template_root" >&2
  exit 1
fi

workspace_root="$(resolve_workspace_root "$target_path" "$project_name")"
assert_no_existing_pm_os "$workspace_root"
copy_template_contents "$template_root" "$workspace_root" "$project_name"

echo "PM OS workspace created: $workspace_root"
echo "Open INDEX.md first, then START_HERE.md, AGENTS.md, and _workspace_setup_docs/personalization/README.md."
echo "To personalize later, tell your agent: Customize my workspace."
