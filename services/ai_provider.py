from services.openai_provider import OpenAIProvider
from services.gemini_provider import GeminiProvider
from services.ollama_provider import OllamaProvider

class AIProviderFactory:

```
@staticmethod
def get_provider(provider_name, api_key=None):

    provider_name = provider_name.lower()

    if provider_name == "ollama":
        return OllamaProvider()

    elif provider_name == "gemini":
        return GeminiProvider(api_key)

    return OpenAIProvider(api_key)
```
