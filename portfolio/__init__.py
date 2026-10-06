import os
from datetime import date

from flask import Flask

from . import content


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY=os.environ.get("SECRET_KEY", "dev-change-me"))
    if test_config:
        app.config.update(test_config)

    @app.context_processor
    def inject_globals():
        return {"profile": content.PROFILE, "year": date.today().year}

    from .views import bp
    app.register_blueprint(bp)

    return app
