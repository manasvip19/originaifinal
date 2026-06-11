import os
import re
import json
import glob

root = os.path.dirname(__file__)
attrs = ['data-i18n', 'data-i18n-placeholder', 'data-i18n-title']
keys = set()

for path in glob.glob(os.path.join(root, 'templates', '*.html')):
    with open(path, 'r', encoding='utf-8') as f:
        txt = f.read()
    for attr in attrs:
        keys.update(re.findall(attr + r'\s*=\s*"([^\"]+)"', txt))

print('TEMPLATE_KEYS_COUNT', len(keys))
for lang in ['en','hi','te','ta']:
    path = os.path.join(root, 'static', 'translations', f'{lang}.json')
    if not os.path.exists(path):
        print('MISSING_FILE', path)
        continue
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    missing = sorted(k for k in keys if k not in data)
    print('LANG', lang, 'KEYS', len(data), 'MISSING', len(missing))
    if missing:
        print('\n'.join(missing))
