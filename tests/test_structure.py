from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_playbook_is_valid_yaml_and_has_expected_sections():
    data = yaml.safe_load((ROOT / "playbook.yml").read_text())
    assert isinstance(data, list) and len(data) == 1
    play = data[0]
    assert play["hosts"] == "webservers"
    assert play["become"] is True
    assert {t["name"] for t in play["tasks"]} >= {
        "Install web server package",
        "Ensure web root exists",
        "Deploy application landing page",
        "Ensure web service is enabled and running",
    }


def test_template_and_inventory_exist():
    assert (ROOT / "templates/index.html.j2").is_file()
    assert (ROOT / "inventory/hosts.ini.example").is_file()
    assert (ROOT / "inventory/local.ini").is_file()


def test_no_private_material_is_committed():
    forbidden = list(ROOT.rglob("*.pem")) + list(ROOT.rglob("*.key"))
    assert forbidden == []
