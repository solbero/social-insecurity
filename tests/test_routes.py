from __future__ import annotations

from collections.abc import Iterator
from typing import TYPE_CHECKING

import pytest

from social_insecurity import app

if TYPE_CHECKING:
    from flask import Flask
    from flask.testing import FlaskClient


@pytest.fixture(scope="session")
def test_app() -> Iterator[Flask]:
    app.config.update(
        {
            "SQLITE3_DATABASE": "file::memory:?cache=shared",
            "TESTING": True,
            "WTF_CSRF_ENABLED": False,
        }
    )
    yield app


@pytest.fixture()
def client(test_app: Flask) -> FlaskClient:
    return test_app.test_client()


def test_request_index(client: FlaskClient):
    response = client.get("/")
    assert response.status_code == 200
