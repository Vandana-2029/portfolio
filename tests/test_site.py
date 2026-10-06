import json
import os

import pytest

from portfolio import create_app
from portfolio.content import PROJECTS


@pytest.fixture
def client(tmp_path):
    app = create_app({"TESTING": True})
    app.instance_path = str(tmp_path)
    return app.test_client()


def test_home_lists_featured_projects(client):
    res = client.get("/")
    assert res.status_code == 200
    html = res.get_data(as_text=True)
    for p in PROJECTS:
        assert p["title"] in html


@pytest.mark.parametrize("slug", [p["slug"] for p in PROJECTS])
def test_project_pages(client, slug):
    assert client.get(f"/projects/{slug}").status_code == 200


def test_unknown_project_is_404(client):
    res = client.get("/projects/does-not-exist")
    assert res.status_code == 404
    assert "Nothing hidden here" in res.get_data(as_text=True)


def test_resume_is_served(client):
    res = client.get("/resume")
    assert res.status_code == 200
    assert res.mimetype == "application/pdf"


def test_contact_rejects_bad_input(client):
    res = client.post("/contact", data={"name": "", "email": "nope", "message": "hi"})
    assert res.status_code == 400
    html = res.get_data(as_text=True)
    assert "Enter your name." in html
    assert "Enter an email address" in html


def test_contact_saves_valid_message(client, tmp_path):
    res = client.post(
        "/contact",
        data={"name": "Asha", "email": "asha@example.com", "message": "Let's talk about a role."},
        follow_redirects=True,
    )
    assert res.status_code == 200
    assert "Thanks, Asha" in res.get_data(as_text=True)
    with open(os.path.join(tmp_path, "messages.jsonl")) as f:
        saved = json.loads(f.readline())
    assert saved["email"] == "asha@example.com"


def test_honeypot_drops_bots(client, tmp_path):
    client.post("/contact", data={"name": "Bot", "email": "b@b.co", "message": "spam spam spam", "website": "x"})
    assert not os.path.exists(os.path.join(tmp_path, "messages.jsonl"))
