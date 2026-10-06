from flask import Blueprint, render_template

from . import content

bp = Blueprint("site", __name__)


@bp.route("/")
def home():
    return render_template("home.html")
