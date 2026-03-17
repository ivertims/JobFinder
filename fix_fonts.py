import os

index_path = r"c:\Users\Student Assistant\Desktop\app\JobFinder\index.html"
variables_path = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\styles\variables.css"

with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

font_tags = """    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
"""

if '<link rel="icon"' in index_content:
    index_content = index_content.replace('<link rel="icon"', font_tags + '    <link rel="icon"')

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)

with open(variables_path, 'r', encoding='utf-8') as f:
    vars_content = f.read()

vars_content = vars_content.replace("font-family: 'Inter',", "font-family: 'Outfit', 'Inter',")

with open(variables_path, 'w', encoding='utf-8') as f:
    f.write(vars_content)

print("Fonts injected and variables updated")
