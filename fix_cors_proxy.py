import os

vite_config = r"c:\Users\Student Assistant\Desktop\app\JobFinder\vite.config.js"
adzuna_js = r"c:\Users\Student Assistant\Desktop\app\JobFinder\src\services\adzuna.js"

# 1. Update vite.config.js
with open(vite_config, 'r', encoding='utf-8') as f:
    config_content = f.read()

target_config = """export default defineConfig({
  plugins: [react()],
})"""

replacement_config = """export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api-adzuna': {
        target: 'https://api.adzuna.com',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api-adzuna/, '')
      }
    }
  }
})"""

if target_config in config_content:
    config_content = config_content.replace(target_config, replacement_config)
else:
    config_content = config_content.replace(target_config.replace('\n', '\r\n'), replacement_config.replace('\n', '\r\n'))

with open(vite_config, 'w', encoding='utf-8') as f:
    f.write(config_content)

# 2. Update adzuna.js to hit proxy instead of direct URL
with open(adzuna_js, 'r', encoding='utf-8') as f:
    js_content = f.read()

# Change fully qualified URL to relative proxy
target_js = "const BASE_URL = 'https://api.adzuna.com/v1/api/jobs/gb/search';"
replacement_js = "const BASE_URL = '/api-adzuna/v1/api/jobs/gb/search';"

if target_js in js_content:
    js_content = js_content.replace(target_js, replacement_js)

with open(adzuna_js, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Vite proxy and Adzuna URL adjusted to bypass CORS")
