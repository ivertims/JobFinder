import os

dashboard_css = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\styles\Dashboard.css"
search_css = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\styles\Search.css"
variables_css = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\styles\variables.css"

# Update Dashboard.css for bottom bar sidebar navigation 
with open(dashboard_css, 'r', encoding='utf-8') as f:
    dash_content = f.read()

responsive_target = """@media (max-width: 1024px) {
  .dashboard-container {
    grid-template-columns: 1fr;
  }
  .sidebar {
    display: none; /* Mobile menu requires toggling */
  }
  .content-grid {
    grid-template-columns: 1fr;
  }
}"""

responsive_replacement = """@media (max-width: 1024px) {
  .dashboard-container {
    grid-template-columns: 1fr;
    height: auto;
    padding-bottom: 70px; /* Add space for bottom nav */
  }

  .sidebar {
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
  }

  .sidebar-logo {
    display: none;
  }

  .sidebar-nav {
    flex-direction: row;
    justify-content: space-around;
    width: 100%;
    gap: 4px;
  }

  .nav-item {
    flex-direction: column;
    align-items: center;
    gap: 4px;
    padding: 6px 12px;
    font-size: 11px;
    border-radius: 8px;
    background: none;
    border: none;
    color: var(--text-muted);
  }

  .nav-item span {
    font-size: 10px;
  }

  .sidebar > div[style*="marginTop: auto"] {
    display: none !important; /* Hide profile and logout on bottom nav to save space */
  }

  .dashboard-main {
    padding: 20px;
  }

  .content-grid {
    grid-template-columns: 1fr;
  }
}"""

if responsive_target in dash_content:
    dash_content = dash_content.replace(responsive_target, responsive_replacement)
else:
    dash_content = dash_content.replace(responsive_target.replace('\n', '\r\n'), responsive_replacement.replace('\n', '\r\n'))

with open(dashboard_css, 'w', encoding='utf-8') as f:
    f.write(dash_content)

# Update Search.css for mobile search wrapping and card stacks
with open(search_css, 'r', encoding='utf-8') as f:
    search_content = f.read()

# Fix search bar breakups on screens < 650px
search_bar_responsive = """@media (max-width: 650px) {
  .search-bar {
    flex-direction: column;
    align-items: stretch;
    padding: 16px;
  }
  .search-divider {
    width: 100%;
    height: 1px;
    margin: 8px 0;
  }
  .search-input-group {
    padding: 8px 0;
  }
}
"""

if search_bar_responsive not in search_content:
    search_content += "\n" + search_bar_responsive

with open(search_css, 'w', encoding='utf-8') as f:
    f.write(search_content)

print("Mobile styles injected")
