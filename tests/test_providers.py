import requests
from services.openai_provider import OpenAIProvider
from services.gemini_provider import GeminiProvider
from services.ollama_provider import OllamaProvider


def test_openai_fallback_when_no_client():
    p = OpenAIProvider(api_key=None)
    out = p.generate("Hello world prompt")
    assert isinstance(out, str)
    assert out.startswith("[OpenAI fallback]")


def test_gemini_fallback_when_no_key():
    p = GeminiProvider(api_key=None)
    out = p.generate("Test prompt for Gemini")
    assert isinstance(out, str)
    assert out.startswith("[Gemini fallback]")


def test_ollama_offline(monkeypatch):
    def raise_conn(*args, **kwargs):
        raise requests.exceptions.ConnectionError("failed")

    monkeypatch.setattr(requests, "post", raise_conn)
    p = OllamaProvider(url="http://localhost:11434", model="llama3")
    out = p.generate("Test prompt")
    assert out == "[Ollama unavailable] Local inference could not be reached"
