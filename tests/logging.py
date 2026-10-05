"""Tests for safe HTTP request diagnostics."""

import logging
from unittest.mock import patch

import pytest
from requests import Response

from gocream_pysberbank import SberbankClient


@pytest.mark.parametrize(
    "credentials",
    [
        {"username": "synthetic-username", "password": "synthetic-password"},
        {"token": "synthetic-token"},
    ],
)
def test_debug_logs_exclude_sensitive_request_and_response_data(caplog, credentials):
    """DEBUG logs contain only method/status for either supported authentication mode."""
    client = SberbankClient(
        **credentials,
        url="https://example.test/{api_type}/{method}?token=synthetic-url-secret",
    )
    response = Response()
    response.status_code = 200
    response._content = b'{"orderId": "synthetic-response-order"}'

    with (
        patch("gocream_pysberbank.http.requests.post", return_value=response) as post,
        caplog.at_level(logging.DEBUG, logger="gocream_pysberbank"),
    ):
        result = client.register(
            "synthetic-request-order",
            12345,
            "https://example.test/return",
            headers={"Authorization": "synthetic-header-secret"},
        )

    post.assert_called_once()
    assert result == {"orderId": "synthetic-response-order"}
    assert caplog.messages == [
        "Making request for method register.do.",
        "Response for method register.do has HTTP status 200.",
    ]
    assert "synthetic" not in caplog.text
