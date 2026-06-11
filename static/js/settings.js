// Settings page logic: store provider and keys in localStorage
document.addEventListener('DOMContentLoaded', () => {
    const provider = document.getElementById('provider');
    const apiKey = document.getElementById('apiKey');
    const ollamaRow = document.getElementById('ollamaRow');
    const ollamaUrl = document.getElementById('ollamaUrl');
    const ollamaModel = document.getElementById('ollamaModel');
    const saveBtn = document.getElementById('saveBtn');
    const testBtn = document.getElementById('testBtn');
    const status = document.getElementById('status');

    function refreshUI() {
        const p = localStorage.getItem('ai_provider') || 'openai';
        provider.value = p;
        apiKey.value = localStorage.getItem('ai_key_' + p) || '';
        ollamaUrl.value = localStorage.getItem('ollama_url') || 'http://localhost:11434';
        ollamaModel.value = localStorage.getItem('ollama_model') || 'llama3';
        ollamaRow.style.display = p === 'ollama' ? 'block' : 'none';
    }

    provider.addEventListener('change', () => {
        const p = provider.value;
        ollamaRow.style.display = p === 'ollama' ? 'block' : 'none';
        apiKey.placeholder = p === 'ollama' ? 'Not required for Ollama' : 'Enter your API key';
    });

    saveBtn.addEventListener('click', () => {
        const p = provider.value;
        localStorage.setItem('ai_provider', p);
        if (p === 'ollama') {
            localStorage.setItem('ollama_url', ollamaUrl.value || 'http://localhost:11434');
            localStorage.setItem('ollama_model', ollamaModel.value || 'llama3');
        } else {
            const key = apiKey.value && apiKey.value.trim();
            if (key) localStorage.setItem('ai_key_' + p, key);
        }
        status.textContent = 'Settings saved locally';
    });

    testBtn.addEventListener('click', async () => {
        status.textContent = '';
        const p = provider.value;
        let payload = { provider: p, prompt: 'Hello from OriginAI - test connection' };
        if (p === 'ollama') {
            payload.ollama_url = ollamaUrl.value || 'http://localhost:11434';
            payload.model = ollamaModel.value || 'llama3';
        } else {
            const key = apiKey.value && apiKey.value.trim();
            if (!key) {
                status.textContent = 'API key missing';
                return;
            }
            payload.api_key = key;
        }

        try {
            const res = await fetch('/api/generate', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
            const data = await res.json();
            if (res.ok && data.result) {
                status.textContent = 'Test successful: ' + String(data.result).slice(0, 120);
            } else {
                status.textContent = 'Test failed: ' + (data.error || JSON.stringify(data));
            }
        } catch (err) {
            status.textContent = 'Network error: ' + err.message;
        }
    });

    refreshUI();
});
