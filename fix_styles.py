import os

variables_path = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\styles\variables.css"
dashboard_path = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\styles\Dashboard.css"

with open(variables_path, 'r', encoding='utf-8') as f:
    vars_content = f.read()

variables_to_replace = """:root {
  --bg-primary: #0b0f19;
  --bg-secondary: #141b2d;
  --glass-bg: rgba(255, 255, 255, 0.03);
  --glass-border: rgba(255, 255, 255, 0.05);
  --glass-hover: rgba(255, 255, 255, 0.08);
  --accent-primary: #4361ee;
  --accent-secondary: #00b4d8;
  --text-active: #ffffff;
  --text-muted: #94a3b8;
  --primary-gradient: linear-gradient(135deg, #4361ee, #00b4d8);
  --danger: #ef4444;
  --success: #10b981;
  --warning: #f59e0b;
}"""

variables_new = """:root {
  /* Common variables */
  --accent-primary: #4361ee;
  --accent-secondary: #00b4d8;
  --primary-gradient: linear-gradient(135deg, #4361ee, #00b4d8);
  --danger: #ef4444;
  --success: #10b981;
  --warning: #f59e0b;

  /* Default (Light Mode) */
  --bg-primary: #f8fafc;
  --bg-secondary: #ffffff;
  --glass-bg: rgba(255, 255, 255, 0.9);
  --glass-border: rgba(0, 0, 0, 0.06);
  --glass-hover: rgba(0, 0, 0, 0.03);
  --text-active: #0f172a;
  --text-muted: #64748b;
  --sidebar-bg: #ffffff;
  --card-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
  --nav-active-bg: rgba(67, 97, 238, 0.08);
  --nav-active-text: #4361ee;
}

/* Dark Mode Overrides */
html.dark {
  --bg-primary: #0b0f19;
  --bg-secondary: #141b2d;
  --glass-bg: rgba(255, 255, 255, 0.03);
  --glass-border: rgba(255, 255, 255, 0.05);
  --glass-hover: rgba(255, 255, 255, 0.08);
  --text-active: #ffffff;
  --text-muted: #94a3b8;
  --sidebar-bg: rgba(20, 27, 45, 0.9);
  --card-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
  --nav-active-bg: rgba(67, 97, 238, 0.15);
  --nav-active-text: #00b4d8;
}"""

if variables_to_replace in vars_content:
    vars_content = vars_content.replace(variables_to_replace, variables_new)
else:
    # Try with \r\n
    vars_content = vars_content.replace(variables_to_replace.replace('\n', '\r\n'), variables_new.replace('\n', '\r\n'))

with open(variables_path, 'w', encoding='utf-8') as f:
    f.write(vars_content)

# Fix Dashboard.css line 12
with open(dashboard_path, 'r', encoding='utf-8') as f:
    dash_content = f.read()

dash_content = dash_content.replace('background: rgba(20, 27, 45, 0.5);', 'background: var(--sidebar-bg);')
dash_content = dash_content.replace('background: rgba(67, 97, 238, 0.1);', 'background: var(--nav-active-bg);')
dash_content = dash_content.replace('color: var(--accent-secondary);', 'color: var(--nav-active-text, var(--accent-secondary));')

with open(dashboard_path, 'w', encoding='utf-8') as f:
    f.write(dash_content)

print("Done adjusting styles")
