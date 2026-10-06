from flask import (Blueprint, abort, current_app, flash, redirect,
                   render_template, request, send_from_directory, url_for)

from . import content
from .contact import save_message, validate

bp = Blueprint("site", __name__)


def render_home(form=None, errors=None, status=200):
    featured = [p for p in content.PROJECTS if p["featured"]]
    more = [p for p in content.PROJECTS if not p["featured"]]
    return render_template(
        "home.html",
        featured=featured,
        more=more,
        skills=content.SKILLS,
        education=content.EDUCATION,
        certificate_groups=content.certificate_groups(),
        form=form or {},
        errors=errors or {},
    ), status


@bp.route("/")
def home():
    return render_home()


@bp.route("/contact", methods=["POST"])
def contact():
    # Hidden field that people never see; bots tend to fill it in.
    if request.form.get("website"):
        return redirect(url_for("site.home") + "#contact")

    data, errors = validate(request.form)
    if errors:
        return render_home(form=data, errors=errors, status=400)

    save_message(current_app.instance_path, data)
    flash(f"Thanks, {data['name']}. Your message is sent and I'll reply to {data['email']}.")
    return redirect(url_for("site.home") + "#contact")


@bp.route("/projects/<slug>")
def project(slug):
    item = content.get_project(slug)
    if item is None:
        abort(404)
    others = [p for p in content.PROJECTS if p["slug"] != slug][:3]
    return render_template("project.html", project=item, others=others)


@bp.route("/resume")
def resume():
    return send_from_directory(
        current_app.static_folder + "/files",
        "Vandana_Kumari_Resume.pdf",
        mimetype="application/pdf",
    )


@bp.app_errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404
