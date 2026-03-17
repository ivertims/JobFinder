import os

search_jsx = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\pages\Search.jsx"

with open(search_jsx, 'r', encoding='utf-8') as f:
    content = f.read()

target = """      if (data.results.length > 0) {
        setSelectedJob(data.results[0]);
      }"""

replacement = """      if (data.results.length > 0 && window.innerWidth > 900) {
        setSelectedJob(data.results[0]);
      }"""

if target in content:
    content = content.replace(target, replacement)
else:
    content = content.replace(target.replace('\n', '\r\n'), replacement.replace('\n', '\r\n'))

with open(search_jsx, 'w', encoding='utf-8') as f:
    f.write(content)

print("Search page selection bug fixed")
