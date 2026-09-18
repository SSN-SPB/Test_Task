from flask import Flask
from .routes import api


def create_app():
    app = Flask(__name__)

    # from app.routes import api
    app.register_blueprint(api)

    return app
