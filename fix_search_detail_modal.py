import os

search_jsx = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\pages\Search.jsx"
search_css = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\styles\Search.css"

with open(search_jsx, 'r', encoding='utf-8') as f:
    jsx_content = f.read()

# Inject Close Button after details panel starts
details_target = """          {selectedJob && (
            <section className="glass-card details-panel">
              <div className="details-header">"""

details_replacement = """          {selectedJob && (
            <section className="glass-card details-panel">
              <button className="mobile-detail-close" onClick={() => setSelectedJob(null)}>Back to List</button>
              <div className="details-header">"""

if details_target in jsx_content:
    jsx_content = jsx_content.replace(details_target, details_replacement)

with open(search_jsx, 'w', encoding='utf-8') as f:
    f.write(jsx_content)

# Update Search.css for full overlay
with open(search_css, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Replace previous replacement rule from fix_mobile_search.py
old_media = """@media (max-width: 900px) {
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

new_media = """@media (max-width: 900px) {
  .search-results-container {
    grid-template-columns: 1fr;
  }
  
  .details-panel {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: calc(100vh - 55px); /* Leave room for bottom nav bar */
    border-radius: 0;
    z-index: 2000;
    background: var(--bg-primary);
    display: flex;
    flex-direction: column;
    padding: 20px;
    overflow-y: auto;
  }
  
  .results-list {
    height: calc(100vh - 180px);
  }

  .mobile-detail-close {
    display: block !important;
    background: var(--accent-primary);
    color: white;
    border: none;
    padding: 10px;
    border-radius: 8px;
    width: fit-content;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    margin-bottom: 12px;
  }
}

.mobile-detail-close {
  display: none;
}"""

if old_media in css_content:
    css_content = css_content.replace(old_media, new_media)
else:
    css_content = css_content.replace(old_media.replace('\n', '\r\n'), new_media.replace('\n', '\r\n'))

with open(search_css, 'w', encoding='utf-8') as f:
    f.write(css_content)

print("Search page modal sheet modal added")
