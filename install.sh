#!/usr/bin/env bash

set -euo pipefail

has() {
  command -v "$1" >/dev/null 2>&1
}

log() {
  printf '==> %s\n' "$*"
}

ensure_uv() {
  if has uvx; then
    return
  fi

  if has uv; then
    return
  fi

  log "Installing uv..."
  curl -LsSf https://astral.sh/uv/install.sh | sh

  export PATH="$HOME/.local/bin:$PATH"

  if ! has uvx; then
    echo "error: uvx is still unavailable after installing uv" >&2
    exit 1
  fi
}

main() {
  ensure_uv
  log "Installing roles with role-forge..."
  uvx role-forge add zrr1999/roles
  log "Done."
}

main "$@"
