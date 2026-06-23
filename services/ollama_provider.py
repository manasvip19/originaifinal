import requests


class OllamaProvider:
    def __init__(
        self,
        model="llama3",
        base_url="http://localhost:11434",
    ):
        self.model = model
        self.base_url = base_url

    def generate(self, prompt):
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
            },
            timeout=120,
        )

        response.raise_for_status()
        data = response.json()

        return data.get("response", "")