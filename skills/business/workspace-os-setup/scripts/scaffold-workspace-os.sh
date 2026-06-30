#!/usr/bin/env bash
set -euo pipefail

business_name=""
target_path="."
workspace_kind="business"
business_category=""
objective=""
primary_use=""
use_current_folder=false
create_folder=false

usage() {
  cat <<'EOF'
Usage:
  scaffold-workspace-os.sh --business-name "Business Name" --target-path "." --use-current-folder
  scaffold-workspace-os.sh --business-name "Client Project" --workspace-kind project --target-path "." --create-folder

Options:
  --business-name      Required business, client, or project name. --project-name is accepted as an alias.
  --workspace-kind     business or project. business creates business-hub-docs; project creates project-docs.
  --business-category  Short category such as interior design, agency, consulting, ecommerce, or local service.
  --objective          Main objective for the workspace.
  --primary-use        Main use, such as client-management, brainstorming, knowledge, operations, projects, or general.
EOF
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --business-name|--project-name)
      business_name="${2:-}"
      shift 2
      ;;
    --workspace-kind)
      workspace_kind="${2:-}"
      shift 2
      ;;
    --business-category)
      business_category="${2:-}"
      shift 2
      ;;
    --objective)
      objective="${2:-}"
      shift 2
      ;;
    --primary-use)
      primary_use="${2:-}"
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

if [ -z "${business_name//[[:space:]]/}" ]; then
  echo "--business-name is required (or use --project-name)." >&2
  usage >&2
  exit 1
fi

if [ "$use_current_folder" = true ] && [ "$create_folder" = true ]; then
  echo "Choose either --use-current-folder or --create-folder, not both." >&2
  exit 1
fi

get_slug() {
  local value="$1"
  local slug

  if [ -z "${value//[[:space:]]/}" ]; then
    printf '%s\n' "workspace-os"
    return
  fi

  slug="$(printf '%s' "$value" |
    tr '[:upper:]' '[:lower:]' |
    sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//')"

  if [ -z "$slug" ]; then
    printf '%s\n' "workspace-os"
  else
    printf '%s\n' "$slug"
  fi
}

normalize_workspace_kind() {
  local value
  value="$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+//; s/-+$//')"

  case "$value" in
    project|client-project|client|client-workspace)
      printf '%s\n' "project"
      ;;
    business|business-hub|hub|"")
      printf '%s\n' "business"
      ;;
    *)
      echo "Unknown workspace kind: $1. Use business or project." >&2
      exit 1
      ;;
  esac
}

docs_root_for_kind() {
  case "$1" in
    project)
      printf '%s\n' "project-docs"
      ;;
    *)
      printf '%s\n' "business-hub-docs"
      ;;
  esac
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

  echo "Target folder is not empty. Re-run with --use-current-folder to add the Workspace OS here, or --create-folder to create a new workspace folder." >&2
  exit 1
}

assert_no_existing_workspace_os() {
  local workspace_root="$1"
  local marker

  if [ ! -d "$workspace_root" ]; then
    return
  fi

  for marker in AGENTS.md INDEX.md agents _workspace_setup_docs business-skills business-hub-docs project-docs; do
    if [ -e "$workspace_root/$marker" ]; then
      echo "The target already looks like a Workspace OS workspace: $workspace_root" >&2
      exit 1
    fi
  done
}

directory_has_entries() {
  [ -n "$(find "$1" -mindepth 1 -maxdepth 1 -print -quit)" ]
}

assert_safe_workspace_root() {
  local workspace_root="$1"
  local base_root="$2"

  assert_no_existing_workspace_os "$workspace_root"

  if [ "$workspace_root" != "$base_root" ] && [ -d "$workspace_root" ] && directory_has_entries "$workspace_root"; then
    echo "Refusing to merge into an existing non-empty workspace folder: $workspace_root" >&2
    exit 1
  fi
}

copy_template_contents() {
  local template_root="$1"
  local workspace_root="$2"
  local name="$3"
  local kind="$4"
  local category="$5"
  local goal="$6"
  local use_case="$7"
  local docs_root
  local today
  docs_root="$(docs_root_for_kind "$kind")"
  today="$(LC_TIME=C date '+%b-%d-%Y')"

  # Check every mapped destination before writing anything so a collision cannot
  # leave behind a partially scaffolded workspace.
  while IFS= read -r -d '' file; do
    local relative
    local destination
    relative="${file#$template_root/}"
    case "$relative" in
      business-hub-docs/*)
        relative="$docs_root/${relative#business-hub-docs/}"
        ;;
    esac
    destination="$workspace_root/$relative"

    if [ -e "$destination" ]; then
      echo "Refusing to overwrite existing file: $destination" >&2
      exit 1
    fi
  done < <(find "$template_root" -type f -print0)

  mkdir -p "$workspace_root"

  while IFS= read -r -d '' file; do
    local relative
    local destination
    local destination_dir
    relative="${file#$template_root/}"
    case "$relative" in
      business-hub-docs/*)
        relative="$docs_root/${relative#business-hub-docs/}"
        ;;
    esac
    destination="$workspace_root/$relative"
    destination_dir="$(dirname "$destination")"

    if [ -e "$destination" ]; then
      echo "Refusing to overwrite existing file: $destination" >&2
      exit 1
    fi

    mkdir -p "$destination_dir"
    cp "$file" "$destination"

    case "$file" in
      *.md|*.mdc|*.txt|*.json)
        if [ -n "${name//[[:space:]]/}" ]; then
          BUSINESS_NAME_VALUE="$name" perl -0pi -e 's/\{\{BUSINESS_NAME\}\}/$ENV{BUSINESS_NAME_VALUE}/g; s/\{\{PROJECT_NAME\}\}/$ENV{BUSINESS_NAME_VALUE}/g' "$destination"
        fi
        if [ -n "${category//[[:space:]]/}" ]; then
          BUSINESS_CATEGORY_VALUE="$category" perl -0pi -e 's/\{\{BUSINESS_CATEGORY\}\}/$ENV{BUSINESS_CATEGORY_VALUE}/g' "$destination"
        fi
        if [ -n "${goal//[[:space:]]/}" ]; then
          OBJECTIVE_VALUE="$goal" perl -0pi -e 's/\{\{OBJECTIVE\}\}/$ENV{OBJECTIVE_VALUE}/g' "$destination"
        fi
        if [ -n "${use_case//[[:space:]]/}" ]; then
          PRIMARY_USE_VALUE="$use_case" perl -0pi -e 's/\{\{PRIMARY_USE\}\}/$ENV{PRIMARY_USE_VALUE}/g' "$destination"
        fi
        DOCS_ROOT_VALUE="$docs_root" WORKSPACE_KIND_VALUE="$kind" DATE_VALUE="$today" perl -0pi -e 's/\{\{DOCS_ROOT\}\}/$ENV{DOCS_ROOT_VALUE}/g; s/\{\{WORKSPACE_KIND\}\}/$ENV{WORKSPACE_KIND_VALUE}/g; s/\{\{DATE\}\}/$ENV{DATE_VALUE}/g' "$destination"
        ;;
    esac
  done < <(find "$template_root" -type f -print0)
}

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
skill_root="$(cd "$script_dir/.." && pwd -P)"
template_root="$skill_root/assets/workspace-os-workspace"

if [ ! -d "$template_root" ]; then
  echo "Missing template folder: $template_root" >&2
  exit 1
fi

workspace_kind="$(normalize_workspace_kind "$workspace_kind")"
workspace_root="$(resolve_workspace_root "$target_path" "$business_name")"
base_root="$(absolute_dir "$target_path")"
assert_safe_workspace_root "$workspace_root" "$base_root"
copy_template_contents "$template_root" "$workspace_root" "$business_name" "$workspace_kind" "$business_category" "$objective" "$primary_use"

echo "Workspace OS workspace created: $workspace_root"
echo "Open INDEX.md first, then START_HERE.md, AGENTS.md, and _workspace_setup_docs/personalization/README.md."
echo "To personalize later, tell your agent: Customize my workspace."
