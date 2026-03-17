import os

map_css = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\styles\MapView.css"

with open(map_css, 'r', encoding='utf-8') as f:
    content = f.read()

rule = """@media (max-width: 768px) {
  .map-floating-details {
    top: auto;
    bottom: 80px; /* Above bottom side navigations */
    right: 16px;
    left: 16px;
    width: auto;
    z-index: 99;
  }
}"""

if rule not in content:
    content += "\n" + rule

with open(map_css, 'w', encoding='utf-8') as f:
    f.write(content)

print("Map responsive fix complete")
