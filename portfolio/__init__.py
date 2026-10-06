from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY="dev-change-me")
    if test_config:
        app.config.update(test_config)

    @app.route("/")
    def home():
        return "Vandana Kumari - portfolio coming soon"

    return app
