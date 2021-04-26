from flask import Flask
from backend.extensions import db, migrate
from backend.blueprints.api import api_bp
from flask_cors import CORS


def register_extensions(app):
    db.app = app
    db.init_app(app)

    migrate.init_app(app, db, render_as_batch=True)


def register_blueprints(app):
    app.register_blueprint(api_bp)


def create_app():
    app = Flask(
        'backend'
    )

    app.config.from_object('backend.settings.BaseConfig')

    # use cors for connecting frontend and backend
    cors = CORS(app, resources={r'/api/*': {'origins': '*'}})

    # register blueprints on the app
    register_blueprints(app)

    # register extensions on the app
    register_extensions(app)

    return app
