import os
from pathlib import Path
import pytest
from falaai_api import Client, AuthenticatedClient

_ENV_FILE = Path(__file__).resolve().parents[3] / ".env.e2e"

def _read(p):
    d = {}
    if p.exists():
        for ln in p.read_text(encoding="utf-8").splitlines():
            ln = ln.strip()
            if ln and not ln.startswith("#") and "=" in ln:
                k, v = ln.split("=", 1)
                d[k.strip()] = v.strip()
    return d

_ENV = _read(_ENV_FILE)

def _get(n):
    v = os.environ.get(n) or _ENV.get(n)
    assert v, f"[E2E] variavel ausente: {n}"
    return v

BASE = os.environ.get("FALAAI_E2E_BASE") or _ENV.get("FALAAI_LOCAL_URL")
KEY = _get("FALAAI_TEST_KEY")
PROD = _get("FALAAI_PROD_URL")
AUDIO = _get("FALAAI_E2E_AUDIO")

@pytest.fixture(scope="session")
def base_url():
    return BASE

@pytest.fixture(scope="session")
def client(base_url):
    return Client(base_url=base_url)

@pytest.fixture(scope="session")
def auth(base_url):
    return AuthenticatedClient(base_url=base_url, token=KEY)