import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix grid columns to prevent overlap
css = css.replace('minmax(300px, 1fr)', 'minmax(380px, 1fr)')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update services.html SVG inline styles
with open('services.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make SVGs responsive
html = re.sub(r'style="height: 80px; width: auto; margin: 0 auto; display: inline-block;"', 
              r'style="height: 80px; max-width: 100%; width: auto; margin: 0 auto; display: inline-block;"', 
              html)

html = html.replace('style.css?v=22', 'style.css?v=23')

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(html)

for file in ['index.html', 'about.html', 'team.html', 'contact.html']:
    with open(file, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('style.css?v=22', 'style.css?v=23')
    with open(file, 'w', encoding='utf-8') as f:
        f.write(c)

print("Fixed services layout")
