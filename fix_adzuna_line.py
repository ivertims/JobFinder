import os

adzuna_js = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\services\adzuna.js"

with open(adzuna_js, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'const BASE_URL =' in line:
        lines[i] = "const BASE_URL = '/api-adzuna/v1/api/jobs/gb/search';\n"
        break

with open(adzuna_js, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("Adzuna URL updated with proxy with comment check safely")
