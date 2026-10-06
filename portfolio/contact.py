import json
import os
import re
from datetime import datetime, timezone

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def validate(form):
    """Return (clean_data, errors) for a submitted contact form."""
    data = {
        "name": form.get("name", "").strip(),
        "email": form.get("email", "").strip(),
        "message": form.get("message", "").strip(),
    }
    errors = {}
    if not data["name"]:
        errors["name"] = "Enter your name."
    elif len(data["name"]) > 100:
        errors["name"] = "Keep your name under 100 characters."
    if not EMAIL_RE.match(data["email"]):
        errors["email"] = "Enter an email address like name@example.com."
    if len(data["message"]) < 10:
        errors["message"] = "Write at least 10 characters so I know how to help."
    elif len(data["message"]) > 2000:
        errors["message"] = "Keep the message under 2000 characters."
    return data, errors


def save_message(instance_path, data):
    os.makedirs(instance_path, exist_ok=True)
    record = dict(data, received_at=datetime.now(timezone.utc).isoformat())
    with open(os.path.join(instance_path, "messages.jsonl"), "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
