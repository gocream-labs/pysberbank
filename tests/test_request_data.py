"""Tests for preparing payment API request parameters."""

from unittest.mock import patch

import pytest
from requests import Response

from gocream_pysberbank import SberbankClient


@pytest.mark.parametrize(
    ("value", "expected"),
    [(0, 0), (False, False), ("", ""), ([], "[]"), ({}, "{}")],
)
def test_make_data_preserves_falsy_values(value, expected):
    """Explicit falsy values survive filtering, with collections encoded as JSON."""
    client = SberbankClient(token="synthetic-token")

    data = client._make_data({"parameter": value})

    assert data["parameter"] == expected
    assert type(data["parameter"]) is type(expected)


@pytest.mark.parametrize("remove_null", [True, False])
def test_make_data_filters_none_only_when_enabled(remove_null):
    """None is omitted by default and retained when filtering is disabled."""
    client = SberbankClient(token="synthetic-token")

    data = client._make_data({"parameter": None}, remove_null=remove_null)

    if remove_null:
        assert "parameter" not in data
    else:
        assert data["parameter"] is None


def test_make_data_does_not_modify_input():
    """Filtering, authentication, and JSON serialization leave input data unchanged."""
    client = SberbankClient(token="synthetic-token")
    params = {"missing": None, "zero": 0, "items": [], "options": {}}

    data = client._make_data(params)

    assert params == {"missing": None, "zero": 0, "items": [], "options": {}}
    assert data is not params


def test_register_sends_zero_tax_system():
    """Registration sends taxSystem=0 in the HTTP payload without optional None values."""
    client = SberbankClient(token="synthetic-token")
    response = Response()
    response.status_code = 200
    response._content = b'{"orderId": "synthetic-order"}'

    with patch("gocream_pysberbank.http.requests.post", return_value=response) as post:
        client.register("synthetic-order", 100, "https://example.test/return", tax_system=0)

    post.assert_called_once()
    data = post.call_args.kwargs["data"]
    assert data["taxSystem"] == 0
    assert "failUrl" not in data
