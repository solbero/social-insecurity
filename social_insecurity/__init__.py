"""Provides the social_insecurity package for the Social Insecurity application. The package contains the Flask app and all of the extensions and routes."""

from pathlib import Path
from shutil import rmtree
from typing import cast

from flask import Flask, current_app

from social_insecurity.config import Config
from social_insecurity.database import SQLite3

# from flask_login import LoginManager
# from flask_bcrypt import Bcrypt
# from flask_wtf.csrf import CSRFProtect

# Instantiate and configure the app
app = Flask(__name__)
app.config.from_object(Config)

# Instantiate the sqlite database extension
sqlite = SQLite3(app, schema="schema.sql")

# TODO: Handle login management better, maybe with flask_login?
# login = LoginManager(app)

# TODO: The passwords are stored in plaintext, this is not secure at all. I should probably use bcrypt or something
# bcrypt = Bcrypt(app)

# TODO: The CSRF protection is not working, I should probably fix that
# csrf = CSRFProtect(app)


@app.cli.command("reset")
def reset_command() -> None:
    """Reset the app."""
    instance_path = Path(current_app.instance_path)
    if instance_path.exists():
        rmtree(instance_path)


# Create the instance and upload folder if they do not exist
with app.app_context():
    instance_path = Path(app.instance_path)
    if not instance_path.exists():
        instance_path.mkdir(parents=True, exist_ok=True)
    upload_path = instance_path / cast(str, app.config["UPLOADS_FOLDER_PATH"])
    if not upload_path.exists():
        upload_path.mkdir(parents=True, exist_ok=True)

# Import the routes after the app is configured
from social_insecurity import routes  # noqa: E402,F401
