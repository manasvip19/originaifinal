import json
from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_api_generate_openai_fallback():
    payload = {"provider": "openai", "prompt": "Hello from test"}
    r = client.post("/api/generate", json=payload)
    assert r.status_code == 200
    data = r.json()
    assert "result" in data
    assert isinstance(data["result"], str)
    assert data["result"].startswith("[OpenAI fallback]")


def test_api_generate_missing_provider():
    payload = {"prompt": "Missing provider test"}
    r = client.post("/api/generate", json=payload)
    assert r.status_code == 400
    data = r.json()
    assert "detail" in data
