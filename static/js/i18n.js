// Simple i18n utility
(function () {
    const defaultLang = 'en';
    let currentLang = localStorage.getItem('originai_lang') || defaultLang;
    let baseTranslations = {};
    let translations = {};

    async function loadJson(path) {
        try {
            const res = await fetch(path);
            if (!res.ok) throw new Error(`Failed to load ${path} (${res.status})`);
            return await res.json();
        } catch (error) {
            console.error('Translation fetch error:', path, error);
            return {};
        }
    }

    async function loadLanguage(lang) {
        currentLang = lang || defaultLang;
        localStorage.setItem('originai_lang', currentLang);
        baseTranslations = await loadJson('/static/translations/en.json');
        if (currentLang === 'en') {
            translations = baseTranslations;
        } else {
            const selected = await loadJson(`/static/translations/${currentLang}.json`);
            translations = Object.assign({}, baseTranslations, selected);
        }
        console.log('Translation file loaded', currentLang, Object.keys(translations).length, 'keys');
        translatePage();
        return translations;
    }

    function t(key) {
        if (!key) return '';
        if (translations && Object.prototype.hasOwnProperty.call(translations, key)) {
            return translations[key];
        }
        if (baseTranslations && Object.prototype.hasOwnProperty.call(baseTranslations, key)) {
            return baseTranslations[key];
        }
        console.warn('Missing translation key:', key);
        return key;
    }

    function translatePage() {
        const elements = document.querySelectorAll('[data-i18n]');
        const placeholderElements = document.querySelectorAll('[data-i18n-placeholder]');
        const valueElements = document.querySelectorAll('[data-i18n-value]');
        let translated = 0;
        const missing = [];

        elements.forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (!key) return;
            const val = t(key);
            if (val === key) missing.push(key);
            if (el.getAttribute('data-i18n-html') === 'true') {
                el.innerHTML = val;
            } else {
                el.innerText = val;
            }
            translated += 1;
        });

        placeholderElements.forEach(el => {
            const key = el.getAttribute('data-i18n-placeholder');
            if (!key) return;
            const val = t(key);
            if (val === key) missing.push(key);
            el.setAttribute('placeholder', val);
            translated += 1;
        });

        valueElements.forEach(el => {
            const key = el.getAttribute('data-i18n-value');
            if (!key) return;
            const val = t(key);
            if (val === key) missing.push(key);
            el.value = val;
            translated += 1;
        });

        console.log('translatePage:', translated, 'elements translated', missing.length, 'missing keys');
        if (missing.length) {
            console.warn('Missing translation keys:', Array.from(new Set(missing)).join(', '));
        }
        document.dispatchEvent(new CustomEvent('i18n:changed', { detail: { lang: currentLang, translated, missing } }));
        return { translated, missing };
    }

    function setupSelector() {
        const sel = document.getElementById('langSelector');
        if (!sel) return;
        sel.value = currentLang;
        sel.addEventListener('change', (event) => {
            const newLang = event.target.value;
            loadLanguage(newLang);
        });
    }

    async function init() {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => {
                setupSelector();
                loadLanguage(currentLang);
            });
        } else {
            setupSelector();
            await loadLanguage(currentLang);
        }
    }

    window.i18n = {
        loadLanguage,
        translatePage,
        t,
        get currentLang() {
            return currentLang;
        }
    };

    init();
})();
