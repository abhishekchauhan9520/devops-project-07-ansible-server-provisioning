#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

python3 - <<'PY'
from pathlib import Path
import yaml
root = Path('.')
play = yaml.safe_load((root/'playbook.yml').read_text())[0]
assert play['hosts'] == 'webservers'
assert play['become'] is True
assert play['handlers'][0]['ansible.builtin.service']['name'] == '{{ web_service }}'
assert '{{ ansible_hostname' in (root/'templates/index.html.j2').read_text()
print('Playbook semantic checks passed.')
PY
