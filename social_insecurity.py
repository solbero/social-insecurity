#!/usr/bin/env python

"""Configured as entry point for the Social Insecurity application.

To start the application enter 'poetry run flask --debug run' in a terminal.

As an alternative, this file can also be run directly with 'poetry run python social_insecurity.py'.
"""

from social_insecurity import create_app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
