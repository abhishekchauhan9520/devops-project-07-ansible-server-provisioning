# Tests

The local test suite validates repository structure and playbook semantics without connecting to a remote host.

For the authoritative Ansible syntax check, GitHub Actions installs `ansible-core` and runs `ansible-playbook --syntax-check` against the local inventory.
