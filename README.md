# Project 07 — Simple Server Provisioning with Ansible

A practical Ansible example that provisions a Debian/Ubuntu web server by installing Nginx, deploying a managed landing page, and ensuring the service is enabled and running.

## What it demonstrates

- Inventory management
- Privilege escalation with `become`
- Idempotent package installation
- Managed file deployment with a Jinja2 template
- Service enablement and startup
- Handler-based service restart
- Local semantic tests
- Automated Ansible syntax validation with GitHub Actions

## Repository layout

```text
.
├── ansible.cfg
├── inventory/
│   ├── hosts.ini.example
│   └── local.ini
├── playbook.yml
├── templates/
│   └── index.html.j2
├── tests/
│   ├── README.md
│   ├── test_playbook_semantics.sh
│   └── test_structure.py
└── .github/workflows/ansible.yml
```

## Run against a real server

1. Copy `inventory/hosts.ini.example` to a local inventory file.
2. Replace the example host and SSH user with your server details.
3. Configure SSH authentication using an agent or a protected key.
4. Run:

```bash
ansible-playbook -i inventory/hosts.ini playbook.yml
```

For a safe preview:

```bash
ansible-playbook -i inventory/hosts.ini playbook.yml --check --diff
```

Do not commit private keys, passwords, or Vault secrets.

## Local validation

The repository tests intentionally avoid changing the local machine. GitHub Actions performs the real Ansible syntax check with `ansible-core` installed in the runner.

## Learning outcome

This project demonstrates the core configuration-management pattern of declaring the desired server state rather than writing imperative SSH command sequences.
