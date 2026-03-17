import os

sidebar_path = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\components\Sidebar.jsx"

with open(sidebar_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add Lucide icons and ThemeContext
import_target = "import { LayoutDashboard, Search, Bookmark, Briefcase, MapPin, LogOut } from 'lucide-react';"
import_replacement = "import { LayoutDashboard, Search, Bookmark, Briefcase, MapPin, LogOut, Sun, Moon } from 'lucide-react';\nimport { useTheme } from '../context/ThemeContext';"

content = content.replace(import_target, import_replacement)

# Hook up toggle 
context_target = """export default function Sidebar() {
  const { logout, user } = useAuth();"""

context_replacement = """export default function Sidebar() {
  const { logout, user } = useAuth();
  const { isDarkMode, toggleTheme } = useTheme();"""

content = content.replace(context_target, context_replacement)

# Inject button above or below Logout
button_target = """        <button onClick={logout} className="nav-item" style={{ background: 'transparent', border: 'none', width: '100%', textAlign: 'left' }}>
          <LogOut size={20} />
          <span>Logout</span>
        </button>"""

button_replacement = """        <button onClick={toggleTheme} className="nav-item" style={{ background: 'transparent', border: 'none', width: '100%', textAlign: 'left' }}>
          {isDarkMode ? <Sun size={20} /> : <Moon size={20} />}
          <span>{isDarkMode ? 'Light Mode' : 'Dark Mode'}</span>
        </button>
        <button onClick={logout} className="nav-item" style={{ background: 'transparent', border: 'none', width: '100%', textAlign: 'left' }}>
          <LogOut size={20} />
          <span>Logout</span>
        </button>"""

if button_target in content:
    content = content.replace(button_target, button_replacement)
else:
    content = content.replace(button_target.replace('\n', '\r\n'), button_replacement.replace('\n', '\r\n'))

with open(sidebar_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Sidebar toggle injected")
