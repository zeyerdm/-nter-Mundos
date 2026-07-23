with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_path = '<path d="M 85 58 C 150 40, 160 20, 130 20 C 100 20, 110 80, 160 80 C 230 80, 330 45, 415 55" fill="none" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" />'
new_path = '''<path d="M 85 58 C 120 68, 160 50, 195 25" fill="none" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" />
                        <path d="M 250 20 C 210 10, 170 20, 170 50 C 170 80, 210 85, 250 75 C 300 65, 360 45, 415 55" fill="none" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" />'''

content = content.replace(old_path, new_path)
content = content.replace('style.css?v=20', 'style.css?v=22')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('services.html', 'r', encoding='utf-8') as f:
    content = f.read()
    
new_path_services = '''<path d="M 85 58 C 120 68, 160 50, 195 25" fill="none" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M 250 20 C 210 10, 170 20, 170 50 C 170 80, 210 85, 250 75 C 300 65, 360 45, 415 55" fill="none" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" />'''
content = content.replace(old_path, new_path_services)
content = content.replace('style.css?v=20', 'style.css?v=22')

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(content)

for file in ['about.html', 'team.html', 'contact.html']:
    with open(file, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace('style.css?v=20', 'style.css?v=22')
    with open(file, 'w', encoding='utf-8') as f:
        f.write(c)

print("Safe update completed")
