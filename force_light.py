import os

filepath = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\context\ThemeContext.jsx"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

target = """  const [isDarkMode, setIsDarkMode] = useState(() => {
    const saved = localStorage.getItem('theme');
    return saved ? saved === 'dark' : false; 
  });"""

# Hardcode to false for now, to reset user session immediately on load
replacement = """  const [isDarkMode, setIsDarkMode] = useState(false);

  // Quick effect to clear previous cached values from testing setup
  useEffect(() => {
    localStorage.removeItem('theme');
  }, []);"""

if target in content:
    content = content.replace(target, replacement)
else:
    content = content.replace(target.replace('\n', '\r\n'), replacement.replace('\n', '\r\n'))

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Forced light theme layout")
