#!/usr/bin/env bash
# Install draw-uml into user-level skill directories (available in every project
# on this machine). Cursor loads ~/.cursor/skills/; it also loads ~/.agents,
# ~/.claude, and ~/.codex skill dirs for compatibility.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="${ROOT}/skills/draw-uml"

if [[ ! -f "${SRC}/SKILL.md" ]]; then
  echo "error: SKILL.md not found at ${SRC}" >&2
  exit 1
fi

name="$(awk '
  /^---[[:space:]]*$/ { fm += 1; next }
  fm == 1 && $1 == "name:" {
    sub(/^name:[[:space:]]*/, "")
    gsub(/["'\'']/, "")
    print
    exit
  }
' "${SRC}/SKILL.md")"

if [[ "${name}" != "draw-uml" ]]; then
  echo "error: skill name must be draw-uml (directory name), got: ${name:-<empty>}" >&2
  exit 1
fi

copy_skill() {
  local dest="$1"
  local dest_parent dest_real src_real

  dest_parent="$(dirname "${dest}")"
  mkdir -p "${dest_parent}"

  src_real="$(cd "${SRC}" && pwd -P)"
  if [[ -e "${dest}" || -L "${dest}" ]]; then
    dest_real="$(cd "${dest}" && pwd -P)"
    if [[ "${dest_real}" == "${src_real}" ]]; then
      echo "skip  ${dest}  (already this skill tree)"
      return 0
    fi
    rm -rf "${dest}"
  fi

  mkdir -p "${dest}"
  if command -v rsync >/dev/null 2>&1; then
    rsync -a \
      --exclude '__pycache__/' \
      --exclude '*.py[cod]' \
      --exclude '.DS_Store' \
      "${SRC}/" "${dest}/"
  else
    cp -a "${SRC}/." "${dest}/"
  fi
  echo "ok    ${dest}"
}

copy_skill "${HOME}/.cursor/skills/draw-uml"
copy_skill "${HOME}/.agents/skills/draw-uml"
copy_skill "${HOME}/.claude/skills/draw-uml"
copy_skill "${HOME}/.codex/skills/draw-uml"

if command -v skills-ref >/dev/null 2>&1; then
  skills-ref validate "${HOME}/.cursor/skills/draw-uml"
else
  echo "note: skills-ref not on PATH; skipped validation"
fi

echo
echo "Installed user-level skill draw-uml."
echo "Cursor personal skills: ${HOME}/.cursor/skills/draw-uml"
echo "To use this skill with Cloud Agents from your laptop, turn on"
echo "Settings → Agents → Sync Skills for Cloud Agents."
