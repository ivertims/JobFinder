import os

sidebar_path = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\components\Sidebar.jsx"
dashboard_css = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\styles\Dashboard.css"

with open(sidebar_path, 'r', encoding='utf-8') as f:
    sidebar_content = f.read()

target_foot = """      <div style={{ marginTop: 'auto', display: 'flex', flexDirection: 'column', gap: '16px' }}>"""
replacement_foot = """      <div className="sidebar-footer" style={{ marginTop: 'auto', display: 'flex', flexDirection: 'column', gap: '16px' }}>"""

target_prof = """          <div style={{ display: 'flex', alignItems: 'center', gap: '10px', padding: '10px' }}>"""
replacement_prof = """          <div className="sidebar-profile" style={{ display: 'flex', alignItems: 'center', gap: '10px', padding: '10px' }}>"""

if target_foot in sidebar_content:
    sidebar_content = sidebar_content.replace(target_foot, replacement_foot)
else:
    sidebar_content = sidebar_content.replace(target_foot.replace('\n', '\r\n'), replacement_foot.replace('\n', '\r\n'))

if target_prof in sidebar_content:
    sidebar_content = sidebar_content.replace(target_prof, replacement_prof)
else:
    sidebar_content = sidebar_content.replace(target_prof.replace('\n', '\r\n'), replacement_prof.replace('\n', '\r\n'))

with open(sidebar_path, 'w', encoding='utf-8') as f:
    f.write(sidebar_content)

# Update Dashboard.css for profile floating
with open(dashboard_css, 'r', encoding='utf-8') as f:
    dash_content = f.read()

# Append layout styles to the @media (max-width: 1024px) media query
media_rule = """  .sidebar-footer .nav-item {
    display: none !important; /* Hide Light/Dark and Logout from bottom nav */
  }

  .sidebar-profile {
    position: fixed;
    top: 12px;
    left: 12px;
    z-index: 10001;
    background: var(--glass-bg);
    border: 1px solid var(--glass-border);
    border-radius: 12px;
    padding: 4px 10px !important;
    box-shadow: var(--card-shadow);
    backdrop-filter: blur(12px);
  }

  .dashboard-main {
    padding-top: 70px; /* Leave space for top profile overlay */
  }"""

if media_rule not in dash_content:
    # Append inside media block
    dash_content = dash_content.replace('.content-grid {\n    grid-template-columns: 1fr;\n  }\n}', '.content-grid {\n    grid-template-columns: 1fr;\n  }\n\n' + media_rule + '\n}')

with open(dashboard_css, 'w', encoding='utf-8') as f:
    f.write(dash_content)

print("Profile floated to top left")
