import re
for file in ['index.html', 'about.html', 'services.html', 'team.html', 'contact.html']:
    with open(file, 'r', encoding='utf-8') as f:
        c = f.read()
    c = re.sub(r'style\.css\?v=\d+', 'style.css?v=20', c)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(c)
