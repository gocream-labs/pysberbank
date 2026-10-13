"""Python client for the legacy SberBank API maintained by YooKassa."""

from gocream_pysberbank.http import SberbankClient
from gocream_pysberbank.http import SberbankPaymentApi


# Compatibility alias used by pysberbank releases up to 0.1.9.
Sberbank = SberbankClient


__all__ = [
    "SberbankClient",
    "SberbankPaymentApi",
    "Sberbank",
    "__version__",
]


__version__ = "1.0.0"
