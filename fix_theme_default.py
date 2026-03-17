import os

filepath = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\context\ThemeContext.jsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

target = """  const [isDarkMode, setIsDarkMode] = useState(() => {
    const saved = localStorage.getItem('theme');
    return saved ? saved === 'dark' : true; 
  });"""

replacement = """  const [isDarkMode, setIsDarkMode] = useState(() => {
    const saved = localStorage.getItem('theme');
    return saved ? saved === 'dark' : false; 
  });"""

if target in content:
    content = content.replace(target, replacement)
else:
    content = content.replace(target.replace('\n', '\r\n'), replacement.replace('\n', '\r\n'))

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Theme defaulted to light")
