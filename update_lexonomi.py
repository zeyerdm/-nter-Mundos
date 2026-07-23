import os
import re

svg_large = '''    <div class="card-header" style="text-align: center; margin-bottom: 1.5rem;">
        <svg viewBox="0 0 500 150" xmlns="http://www.w3.org/2000/svg" class="product-logo-svg lexonomi-logo" style="height: 80px; width: auto; margin: 0 auto; display: inline-block;">
          <g fill="var(--accent-primary)" stroke="var(--accent-primary)">
            <circle cx="60" cy="55" r="8" stroke="none" />
            <circle cx="440" cy="55" r="8" stroke="none" />
            <path d="M 85 58 C 150 65, 180 40, 190 20 C 195 0, 165 -5, 155 15 C 145 40, 160 75, 200 75 C 280 75, 360 45, 415 55" fill="none" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" />
            <text x="255" y="125" font-family="'Inter', sans-serif" font-weight="700" font-size="32" letter-spacing="16" text-anchor="middle" stroke="none">LEXONOMI</text>
          </g>
        </svg>
    </div>'''

svg_small = '''<div class="card-header">
                    <svg viewBox="0 0 500 150" xmlns="http://www.w3.org/2000/svg" style="height: 30px; width: auto; display: inline-block; vertical-align: middle;">
                      <g fill="var(--accent-primary)" stroke="var(--accent-primary)">
                        <circle cx="60" cy="55" r="8" stroke="none" />
                        <circle cx="440" cy="55" r="8" stroke="none" />
                        <path d="M 85 58 C 150 65, 180 40, 190 20 C 195 0, 165 -5, 155 15 C 145 40, 160 75, 200 75 C 280 75, 360 45, 415 55" fill="none" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" />
                        <text x="255" y="125" font-family="'Inter', sans-serif" font-weight="700" font-size="32" letter-spacing="16" text-anchor="middle" stroke="none">LEXONOMI</text>
                      </g>
                    </svg>
                </div>'''

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<div class="card-header">\s*<i class="fa-solid fa-scale-balanced"></i> Lexonomi\s*</div>', svg_small, content)
content = re.sub(r'style\.css\?v=\d+', 'style.css?v=17', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Update services.html
with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<div class="card-header">\s*<div class="card-icon"><i class="fa-solid fa-scale-balanced"></i></div>\s*<h3>Lexonomi</h3>\s*</div>', svg_large, content)
content = re.sub(r'style\.css\?v=\d+', 'style.css?v=17', content)

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Update other files CSS version just in case
for file in ['about.html', 'team.html', 'contact.html']:
    with open(file, 'r', encoding='utf-8') as f:
        c = f.read()
    c = re.sub(r'style\.css\?v=\d+', 'style.css?v=17', c)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(c)

print("Lexonomi logo updated!")
