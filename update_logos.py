import os
import re

# TAXONOMI
taxonomi_large = '''    <div class="card-header" style="text-align: center; margin-bottom: 1.5rem;">
        <svg viewBox="0 0 500 150" xmlns="http://www.w3.org/2000/svg" class="product-logo-svg taxonomi-logo" style="height: 80px; width: auto; margin: 0 auto; display: inline-block;">
          <g fill="var(--accent-primary)" stroke="var(--accent-primary)">
            <circle cx="60" cy="55" r="8" stroke="none" />
            <circle cx="440" cy="55" r="8" stroke="none" />
            <path d="M 85 58 C 130 68, 180 68, 225 48" fill="none" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" />
            <path d="M 270 28 C 250 20, 225 25, 225 48 C 220 75, 230 85, 260 70 C 310 50, 360 50, 415 55" fill="none" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" />
            <text x="255" y="125" font-family="Georgia, 'Times New Roman', serif" font-weight="600" font-size="32" letter-spacing="14" text-anchor="middle" stroke="none">TAXONOMI</text>
          </g>
        </svg>
    </div>'''

taxonomi_small = '''<div class="card-header">
                    <svg viewBox="0 0 500 150" xmlns="http://www.w3.org/2000/svg" style="height: 30px; width: auto; display: inline-block; vertical-align: middle;">
                      <g fill="var(--accent-primary)" stroke="var(--accent-primary)">
                        <circle cx="60" cy="55" r="8" stroke="none" />
                        <circle cx="440" cy="55" r="8" stroke="none" />
                        <path d="M 85 58 C 130 68, 180 68, 225 48" fill="none" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" />
                        <path d="M 270 28 C 250 20, 225 25, 225 48 C 220 75, 230 85, 260 70 C 310 50, 360 50, 415 55" fill="none" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" />
                        <text x="255" y="125" font-family="Georgia, 'Times New Roman', serif" font-weight="600" font-size="32" letter-spacing="14" text-anchor="middle" stroke="none">TAXONOMI</text>
                      </g>
                    </svg>
                </div>'''

# CHRONOMI
chronomi_large = '''    <div class="card-header" style="text-align: center; margin-bottom: 1.5rem;">
        <svg viewBox="0 0 500 150" xmlns="http://www.w3.org/2000/svg" class="product-logo-svg chronomi-logo" style="height: 80px; width: auto; margin: 0 auto; display: inline-block;">
          <g fill="var(--accent-primary)" stroke="var(--accent-primary)">
            <circle cx="60" cy="55" r="8" stroke="none" />
            <circle cx="440" cy="55" r="8" stroke="none" />
            <path d="M 85 58 C 150 40, 160 20, 130 20 C 100 20, 110 80, 160 80 C 230 80, 330 45, 415 55" fill="none" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" />
            <text x="255" y="125" font-family="'Inter', sans-serif" font-weight="700" font-size="32" letter-spacing="14" text-anchor="middle" stroke="none">CHRONOMI</text>
          </g>
        </svg>
    </div>'''

chronomi_small = '''<div class="card-header">
                    <svg viewBox="0 0 500 150" xmlns="http://www.w3.org/2000/svg" style="height: 30px; width: auto; display: inline-block; vertical-align: middle;">
                      <g fill="var(--accent-primary)" stroke="var(--accent-primary)">
                        <circle cx="60" cy="55" r="8" stroke="none" />
                        <circle cx="440" cy="55" r="8" stroke="none" />
                        <path d="M 85 58 C 150 40, 160 20, 130 20 C 100 20, 110 80, 160 80 C 230 80, 330 45, 415 55" fill="none" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" />
                        <text x="255" y="125" font-family="'Inter', sans-serif" font-weight="700" font-size="32" letter-spacing="14" text-anchor="middle" stroke="none">CHRONOMI</text>
                      </g>
                    </svg>
                </div>'''

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<div class="card-header">\s*<i class="fa-solid fa-file-invoice-dollar"></i> Taxonomi\s*</div>', taxonomi_small, content)
content = re.sub(r'<div class="card-header">\s*<i class="fa-solid fa-clock-rotate-left"></i> Chronomi\s*</div>', chronomi_small, content)
content = re.sub(r'style\.css\?v=\d+', 'style.css?v=18', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Update services.html
with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'<div class="card-icon"[^>]*><i class="fa-solid fa-file-invoice-dollar"></i></div>\s*<h3>Taxonomi</h3>', taxonomi_large, content)
content = re.sub(r'<div class="card-header">\s*(<div class="card-icon"[^>]*><i class="fa-solid fa-file-invoice-dollar"></i></div>\s*<h3>Taxonomi</h3>)\s*</div>', taxonomi_large, content)
content = re.sub(r'<div class="card-icon"[^>]*><i class="fa-solid fa-clock-rotate-left"></i></div>\s*<h3>Chronomi</h3>', chronomi_large, content)

content = re.sub(r'style\.css\?v=\d+', 'style.css?v=18', content)

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Update other files
for file in ['about.html', 'team.html', 'contact.html']:
    with open(file, 'r', encoding='utf-8') as f:
        c = f.read()
    c = re.sub(r'style\.css\?v=\d+', 'style.css?v=18', c)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(c)

print("Taxonomi and Chronomi logos updated!")
