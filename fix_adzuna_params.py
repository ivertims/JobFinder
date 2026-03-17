import os

adzuna_js = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\services\adzuna.js"

with open(adzuna_js, 'r', encoding='utf-8') as f:
    js_content = f.read()

target = """        results_per_page: 20,
        content_type: 'application/json'"""

replacement = """        results_per_page: 20"""

if target in js_content:
    js_content = js_content.replace(target, replacement)
else:
    js_content = js_content.replace(target.replace('\n', '\r\n'), replacement.replace('\n', '\r\n'))

with open(adzuna_js, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Adzuna malformed content_type param removed")
