# Vandana Kumari - Portfolio

Personal portfolio built with **Flask, Jinja, HTML, CSS and vanilla JavaScript**.

The hero is a pixel grid with a message hidden in it, a nod to my SecureSteg
project: move the pointer across it (or press "Reveal message") to read it.

## Features
- Jinja templates with a shared base layout and macros
- Project detail pages at `/projects/<slug>`, generated from one content file
- Contact form with server-side validation, a spam honeypot, and messages saved to `instance/messages.jsonl`
- Resume served at `/resume`
- Light and dark themes (follows the system setting), responsive down to phones, keyboard accessible
- pytest suite

## Project structure
```
portfolio/
  __init__.py      app factory
  views.py         routes
  content.py       all text on the site - edit this to update it
  contact.py       form validation and storage
  templates/       Jinja templates
  static/          CSS, JS, resume PDF
tests/             pytest suite
run.py             entry point
```

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
FLASK_DEBUG=1 python run.py      # Windows: set FLASK_DEBUG=1 && python run.py
```
Open http://127.0.0.1:5000

Run tests with `pytest`.

## Deploy (Render, free tier)
1. Push this repo to GitHub.
2. On render.com create a **Web Service** from the repo.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn run:app`
5. Add an environment variable `SECRET_KEY` with any long random string.

Note: on free hosts the disk resets on redeploy, so saved contact messages
are temporary. Check `instance/messages.jsonl` or switch to a database if you
need them to persist.
