import os

dashboard_css = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\styles\Dashboard.css"

with open(dashboard_css, 'r', encoding='utf-8') as f:
    content = f.read()

# Make sidebar and nav-item compact
target_sidebar = """  .sidebar {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    height: auto;
    background: var(--bg-secondary);
    border-top: 1px solid var(--glass-border);
    border-right: none;
    padding: 8px 16px;
    flex-direction: row;
    justify-content: space-around;
    z-index: 999;
    backdrop-filter: blur(12px);
    gap: 0;
  }"""

replacement_sidebar = """  .sidebar {
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

target_nav_item = """  .nav-item {
    flex-direction: column;
    align-items: center;
    gap: 4px;
    padding: 6px 12px;
    font-size: 11px;
    border-radius: 8px;
    background: none;
    border: none;
    color: var(--text-muted);
  }"""

replacement_nav_item = """  .nav-item {
    flex-direction: column;
    align-items: center;
    gap: 2px; /* Less gap */
    padding: 4px 8px; /* Less padding */
    font-weight: 500;
    font-size: 9px; /* Small font */
    border-radius: 8px;
    background: none;
    border: none;
    color: var(--text-muted);
  }"""

target_dashboard_container = """  .dashboard-container {
    grid-template-columns: 1fr;
    height: auto;
    padding-bottom: 70px; /* Add space for bottom nav */
  }"""

replacement_dashboard_container = """  .dashboard-container {
    grid-template-columns: 1fr;
    height: auto;
    padding-bottom: 50px; /* Reduced space matching compact nav */
  }"""

if target_sidebar in content:
    content = content.replace(target_sidebar, replacement_sidebar)
else:
    content = content.replace(target_sidebar.replace('\n', '\r\n'), replacement_sidebar.replace('\n', '\r\n'))

if target_nav_item in content:
    content = content.replace(target_nav_item, replacement_nav_item)
else:
    content = content.replace(target_nav_item.replace('\n', '\r\n'), replacement_nav_item.replace('\n', '\r\n'))

if target_dashboard_container in content:
    content = content.replace(target_dashboard_container, replacement_dashboard_container)
else:
    content = content.replace(target_dashboard_container.replace('\n', '\r\n'), replacement_dashboard_container.replace('\n', '\r\n'))

with open(dashboard_css, 'w', encoding='utf-8') as f:
    f.write(content)

print("Sidebar made compact")
