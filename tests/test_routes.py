from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING

import pytest

from social_insecurity import create_app

if TYPE_CHECKING:
    from flask import Flask
    from flask.testing import FlaskClient


@pytest.fixture(scope="session")
def app() -> Iterator[Flask]:
    test_config = {
        "SQLITE3_DATABASE_PATH": "file::memory:?cache=shared",
        "TESTING": True,
        "WTF_CSRF_ENABLED": False,
    }
    app = create_app(test_config)
    yield app


@pytest.fixture()
def client(app: Flask) -> FlaskClient:
    return app.test_client()


def test_request_index(client: FlaskClient):
    response = client.get("/")
    assert response.status_code == 200
