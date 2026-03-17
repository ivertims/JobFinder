import os

dashboard_css = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\styles\Dashboard.css"

with open(dashboard_css, 'r', encoding='utf-8') as f:
    content = f.read()

target = """  .sidebar-nav {
    flex-direction: row;
    justify-content: space-around;
    width: 100%;
    gap: 4px;
  }"""

replacement = """  .sidebar-nav {
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
    width: 100%;
    gap: 4px;
  }"""

if target in content:
    content = content.replace(target, replacement)
else:
    content = content.replace(target.replace('\n', '\r\n'), replacement.replace('\n', '\r\n'))

with open(dashboard_css, 'w', encoding='utf-8') as f:
    f.write(content)

print("Bottom bar height stretch fixed")
