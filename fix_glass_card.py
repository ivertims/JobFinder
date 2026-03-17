import os

variables_path = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\styles\variables.css"

with open(variables_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = """.glass-card {
  background: var(--glass-bg);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid var(--glass-border);
  border-radius: 16px;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.glass-card:hover {
  background: var(--glass-hover);
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
}"""

replacement = """.glass-card {
  background: var(--glass-bg);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid var(--glass-border);
  border-radius: 16px;
  box-shadow: var(--card-shadow);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.glass-card:hover {
  background: var(--glass-hover);
  transform: translateY(-2px);
}"""

if target in content:
    content = content.replace(target, replacement)
else:
    content = content.replace(target.replace('\n', '\r\n'), replacement.replace('\n', '\r\n'))

with open(variables_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Glass card style updated")
