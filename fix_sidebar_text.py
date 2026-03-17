import os

dashboard_css = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\styles\Dashboard.css"

with open(dashboard_css, 'r', encoding='utf-8') as f:
    content = f.read()

target = """  .nav-item span {
    font-size: 10px;
  }"""

replacement = """  .nav-item span {
    font-size: 10px;
    white-space: nowrap; /* Prevent breaking lines to match spacing */
  }"""

if target in content:
    content = content.replace(target, replacement)
else:
    content = content.replace(target.replace('\n', '\r\n'), replacement.replace('\n', '\r\n'))

with open(dashboard_css, 'w', encoding='utf-8') as f:
    f.write(content)

print("Nav item text wrapping fixed")
