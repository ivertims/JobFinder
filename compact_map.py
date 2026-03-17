import os

map_css = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\styles\MapView.css"

with open(map_css, 'r', encoding='utf-8') as f:
    content = f.read()

target = """    bottom: 80px; /* Above bottom side navigations */"""
replacement = """    bottom: 60px; /* Above bottom side navigations */"""

if target in content:
    content = content.replace(target, replacement)
else:
    content = content.replace(target.replace('\n', '\r\n'), replacement.replace('\n', '\r\n'))

with open(map_css, 'w', encoding='utf-8') as f:
    f.write(content)

print("Map updated to match compact nav")
