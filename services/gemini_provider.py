import requests


class GeminiProvider:

    def __init__(self, api_key=None):
        self.api_key = api_key

    def _has_key(self):
        return bool(self.api_key)

    def generate(self, prompt):
        if not self._has_key():
            return "[Gemini fallback] " + (prompt[:400] + "...")

        try:
            # Placeholder - Gemini HTTP API endpoint may differ; keep generic and tolerant
            resp = requests.post(
                "https://api.gemini.example/v1/generate",
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={"prompt": prompt, "max_tokens": 512}
            )
            resp.raise_for_status()
            data = resp.json()
            return data.get("text") or data.get("result") or ""
        except Exception:
            return "[Gemini error] Failed to generate response"

    def summarize(self, text):
        prompt = f"Summarize the following text:\n\n{text}"
        return self.generate(prompt)

    def analyze(self, text):
        prompt = f"Extract key discoveries, opportunities and risks from:\n\n{text}"
        return self.generate(prompt)
