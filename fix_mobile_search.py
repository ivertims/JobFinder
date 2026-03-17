import os

search_css = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\styles\Search.css"

with open(search_css, 'r', encoding='utf-8') as f:
    search_content = f.read()

# Replace absolute hiding details-panel
target = """@media (max-width: 900px) {
  .search-results-container {
    grid-template-columns: 1fr;
  }
  .details-panel {
    display: none; /* In mobile view, render full details page / modal */
  }
}"""

# Stack them below lists natively
replacement = """@media (max-width: 900px) {
  .search-results-container {
    grid-template-columns: 1fr;
    height: auto; /* Remove fixed height on mobile */
  }
  
  .details-panel {
    display: flex; /* Show card below instead of hiding */
    padding: 20px;
    height: auto;
  }
  
  .search-main {
    padding: 16px;
    height: auto;
  }
}"""

if target in search_content:
    search_content = search_content.replace(target, replacement)
else:
    search_content = search_content.replace(target.replace('\n', '\r\n'), replacement.replace('\n', '\r\n'))

with open(search_css, 'w', encoding='utf-8') as f:
    f.write(search_content)

print("Search page mobile detailed stacking complete")
