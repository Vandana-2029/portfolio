from flask import Blueprint, abort, render_template

from . import content

bp = Blueprint("site", __name__)


@bp.route("/")
def home():
    featured = [p for p in content.PROJECTS if p["featured"]]
    more = [p for p in content.PROJECTS if not p["featured"]]
    return render_template(
        "home.html", featured=featured, more=more, skills=content.SKILLS
    )


@bp.route("/projects/<slug>")
def project(slug):
    item = content.get_project(slug)
    if item is None:
        abort(404)
    others = [p for p in content.PROJECTS if p["slug"] != slug][:3]
    return render_template("project.html", project=item, others=others)
