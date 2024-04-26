"""Provides the social_insecurity package for the Social Insecurity application.

The package contains the Flask application factory.
"""

from pathlib import Path
from shutil import rmtree
from typing import cast

from flask import Flask, current_app

from social_insecurity.config import Config
from social_insecurity.database import SQLite3

# from flask_login import LoginManager
# from flask_bcrypt import Bcrypt
# from flask_wtf.csrf import CSRFProtect

sqlite = SQLite3()
# TODO: Handle login management better, maybe with flask_login?
# login = LoginManager()
# TODO: The passwords are stored in plaintext, this is not secure at all. I should probably use bcrypt or something
# bcrypt = Bcrypt()
# TODO: The CSRF protection is not working, I should probably fix that
# csrf = CSRFProtect()


def create_app(test_config=None) -> Flask:
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)
    if test_config:
        app.config.from_object(test_config)

    sqlite.init_app(app, schema="schema.sql")
    # login.init_app(app)
    # bcrypt.init_app(app)
    # csrf.init_app(app)

    with app.app_context():
        create_uploads_folder(app)

    @app.cli.command("reset")
    def reset_command() -> None:
        """Reset the app."""
        instance_path = Path(current_app.instance_path)
        if instance_path.exists():
            rmtree(instance_path)

    with app.app_context():
        import social_insecurity.routes  # noqa: E402,F401

    return app


def create_uploads_folder(app: Flask) -> None:
    """Create the instance and upload folders."""
    upload_path = Path(app.instance_path) / cast(str, app.config["UPLOADS_FOLDER_PATH"])
    if not upload_path.exists():
        upload_path.mkdir(parents=True)
