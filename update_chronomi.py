import re

chronomi_large = '''<svg viewBox="0 0 500 150" xmlns="http://www.w3.org/2000/svg" class="product-logo-svg chronomi-logo" style="height: 80px; width: auto; margin: 0 auto; display: inline-block;">
          <g fill="var(--accent-primary)" stroke="var(--accent-primary)">
            <circle cx="60" cy="55" r="8" stroke="none" />
            <circle cx="440" cy="55" r="8" stroke="none" />
            <!-- Left connection line -->
            <path d="M 85 58 C 120 68, 160 50, 195 25" fill="none" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" />
            <!-- The "C" and right sweep -->
            <path d="M 250 20 C 210 10, 170 20, 170 50 C 170 80, 210 85, 250 75 C 300 65, 360 45, 415 55" fill="none" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" />
            <text x="255" y="125" font-family="'Inter', sans-serif" font-weight="700" font-size="32" letter-spacing="14" text-anchor="middle" stroke="none">CHRONOMI</text>
          </g>
        </svg>'''

chronomi_small = '''<svg viewBox="0 0 500 150" xmlns="http://www.w3.org/2000/svg" style="height: 30px; width: auto; display: inline-block; vertical-align: middle;">
                      <g fill="var(--accent-primary)" stroke="var(--accent-primary)">
                        <circle cx="60" cy="55" r="8" stroke="none" />
                        <circle cx="440" cy="55" r="8" stroke="none" />
                        <path d="M 85 58 C 120 68, 160 50, 195 25" fill="none" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" />
                        <path d="M 250 20 C 210 10, 170 20, 170 50 C 170 80, 210 85, 250 75 C 300 65, 360 45, 415 55" fill="none" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" />
                        <text x="255" y="125" font-family="'Inter', sans-serif" font-weight="700" font-size="32" letter-spacing="14" text-anchor="middle" stroke="none">CHRONOMI</text>
                      </g>
                    </svg>'''

# Index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace small svg
content = re.sub(r'<svg viewBox="0 0 500 150"[^>]*>[\s\S]*?<text [^>]*>CHRONOMI</text>[\s\S]*?</svg>', chronomi_small, content)
content = re.sub(r'style\.css\?v=\d+', 'style.css?v=21', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Services.html
with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace large svg
content = re.sub(r'<svg viewBox="0 0 500 150"[^>]*>[\s\S]*?<text [^>]*>CHRONOMI</text>[\s\S]*?</svg>', chronomi_large, content)
content = re.sub(r'style\.css\?v=\d+', 'style.css?v=21', content)

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Update other files CSS version
for file in ['about.html', 'team.html', 'contact.html']:
    with open(file, 'r', encoding='utf-8') as f:
        c = f.read()
    c = re.sub(r'style\.css\?v=\d+', 'style.css?v=21', c)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(c)

print("Chronomi logo updated to C shape!")
