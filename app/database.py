"""Provides a SQLite3 database extension for Flask.

This extension provides a simple interface to the SQLite3 database.

Example:
    from flask import Flask
    from app.database import SQLite3

    app = Flask(__name__)
    db = SQLite3(app)
"""

from __future__ import annotations

import os
import sqlite3
from typing import Any, Optional

from flask import Flask, current_app, g


class SQLite3:
    """Provides a SQLite3 database extension for Flask.

    This class provides a simple interface to the SQLite3 database.
    It also initializes the database if it does not exist yet.

    Example:
        from flask import Flask
        from app.database import SQLite3

        app = Flask(__name__)
        db = SQLite3(app)

        # Use the database
        # db.query("SELECT * FROM Users;")
        # db.query("SELECT * FROM Users WHERE id = 1;", one=True)
        # db.query("INSERT INTO Users (name, email) VALUES ('John', 'test@test.net');")
    """

    def __init__(self, app: Optional[Flask] = None, path: Optional[str] = None) -> None:
        if app is not None:
            self.init_app(app, path)

    def init_app(self, app: Flask, path: Optional[str] = None) -> None:
        """Initializes the application with the extension."""
        if not hasattr(app, "extensions"):
            app.extensions = {}

        if "sqlite3" not in app.extensions:
            app.extensions["sqlite3"] = self
        else:
            raise RuntimeError("Flask SQLite3 extension already initialized")

        if path:
            app.config["SQLITE3_DATABASE_PATH"] = path

        if not app.config["SQLITE3_DATABASE_PATH"]:
            app.config["SQLITE3_DATABASE_PATH"] = "sqlite3.db"

        if app.config["SQLITE3_DATABASE_PATH"] != ":memory:":
            app.config["SQLITE3_DATABASE_PATH"] = os.path.join(app.instance_path, app.config["SQLITE3_DATABASE_PATH"])

        with app.app_context():
            self._init_database()
        app.teardown_appcontext(self._close_connection)

    @property
    def connection(self) -> sqlite3.Connection:
        """Returns the connection to the SQLite3 database."""
        connection = getattr(g, "flask_sqlite3_connection", None)
        if connection is None:
            connection = g.flask_sqlite3_connection = sqlite3.connect(current_app.config["SQLITE3_DATABASE_PATH"])
            connection.row_factory = sqlite3.Row
        return connection

    def query(self, query: str, one: bool = False, *args) -> Any:
        """Queries the database and returns the result.'

        params:
            query: The SQL query to execute.
            one: Whether to return a single row or a list of rows.
            args: Additional arguments to pass to the query.

        returns: A single row, a list of rows or None.

        """
        cursor = self.connection.execute(query, args)
        response = cursor.fetchone() if one else cursor.fetchall()
        cursor.close()
        self.connection.commit()
        return response

    # TODO: Add more specific query methods to simplify code

    def _init_database(self) -> None:
        if not os.path.exists(current_app.instance_path):
            os.makedirs(current_app.instance_path)

        if not os.path.exists(current_app.config["SQLITE3_DATABASE_PATH"]):
            with current_app.open_resource("schema.sql", mode="r") as file:
                self.connection.executescript(file.read())
                self.connection.commit()

    def _close_connection(self, exception: Optional[BaseException] = None) -> None:
        connection = getattr(g, "flask_sqlite3_connection", None)
        if connection is not None:
            connection.close()
