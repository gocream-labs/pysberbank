"""Tests for the package's public imports."""

from gocream_pysberbank import Sberbank
from gocream_pysberbank import SberbankClient
from gocream_pysberbank import SberbankPaymentApi


def test_legacy_client_names_remain_compatible():
    """The previous client names resolve to the canonical SberbankClient class."""
    assert Sberbank is SberbankClient
    assert SberbankPaymentApi is SberbankClient
