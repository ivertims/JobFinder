import os

dashboard_css = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\styles\Dashboard.css"

with open(dashboard_css, 'r', encoding='utf-8') as f:
    content = f.read()

target = """  .sidebar {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    height: auto;
    background: var(--bg-secondary);
    border-top: 1px solid var(--glass-border);
    border-right: none;
    padding: 4px 8px; /* Compact padding */
    flex-direction: row;
    justify-content: space-around;
    z-index: 999;
    backdrop-filter: blur(12px);
    gap: 0;
  }"""

# Set absolute height and align files setup natively triggers
replacement = """  .sidebar {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 55px; /* Force flat compact height */
    background: var(--bg-secondary);
    border-top: 1px solid var(--glass-border);
    border-right: none;
    padding: 0 8px; /* Remove top/bottom padding to let items fit height */
    display: flex;
    align-items: center;
    flex-direction: row;
    justify-content: space-around;
    z-index: 999;
    backdrop-filter: blur(12px);
    gap: 0;
  }"""

if target in content:
    content = content.replace(target, replacement)
else:
    content = content.replace(target.replace('\n', '\r\n'), replacement.replace('\n', '\r\n'))

with open(dashboard_css, 'w', encoding='utf-8') as f:
    f.write(content)

print("Sidebar absolute height fixed")
