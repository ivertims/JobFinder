import os

sidebar_path = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\components\Sidebar.jsx"
dashboard_css = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\styles\Dashboard.css"

with open(sidebar_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add class to Search Link to allow hiding it
search_target = """        <NavLink to="/search" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
          <Search size={20} />
          <span>Search Jobs</span>
        </NavLink>"""

search_replacement = """        <NavLink to="/search" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''} nav-search`}>
          <Search size={20} />
          <span>Search Jobs</span>
        </NavLink>"""

content = content.replace(search_target, search_replacement)

# 2. Inject a separate mobile-profile container right after Dashboard (NavLink 1)
dashboard_target = """        <NavLink to="/" className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}>
          <LayoutDashboard size={20} />
          <span>Dashboard</span>
        </NavLink>"""

# Duplicate profile inside layout structure
mobile_profile = """        {user && (
          <div className="nav-item sidebar-profile-nav">
             <img 
               src={user.photoURL || 'https://via.placeholder.com/40'} 
               alt="Profile" 
               style={{ width: '24px', height: '24px', borderRadius: '50%' }}
             />
             <span>{user.displayName ? (user.displayName.split(' ')[0]) : 'User'}</span>
          </div>
        )}"""

content = content.replace(dashboard_target, dashboard_target + "\n" + mobile_profile)

with open(sidebar_path, 'w', encoding='utf-8') as f:
    f.write(content)

# Update Dashboard.css for profile floating
with open(dashboard_css, 'r', encoding='utf-8') as f:
    dash_content = f.read()

# Remove the previous fixed profile floating styles
extra_styles = """  .sidebar-footer .nav-item {
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

dash_content = dash_content.replace(extra_styles, '')

# Append correct mobile styles
mobile_nav_rules = """  /* Hide search from bottom nav */
  .nav-search {
    display: none !important;
  }

  /* Desktop Profile Hide */
  .sidebar-profile-nav {
    display: none !important;
  }

  @media (max-width: 1024px) {
    .sidebar-profile-nav {
      display: flex !important;
      flex-direction: column;
      align-items: center;
      gap: 2px;
      padding: 4px 8px;
      font-size: 9px;
      color: var(--text-muted);
    }
    
    .sidebar-footer {
      display: none !important;
    }
    
    /* Reset padding-top from previous step safely */
    .dashboard-main {
      padding-top: 20px;
    }
  }"""

if mobile_nav_rules not in dash_content:
    dash_content += "\n" + mobile_nav_rules

with open(dashboard_css, 'w', encoding='utf-8') as f:
    f.write(dash_content)

print("Nav profile swapped onto nav Search")
