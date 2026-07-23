const fs = require('fs');
const files = ['index.html', 'about.html', 'services.html', 'team.html', 'contact.html'];
const newLogo = <a href="index.html" class="logo">
            <svg viewBox="0 0 500 150" xmlns="http://www.w3.org/2000/svg" class="nav-logo-svg">
              <g fill="var(--accent-primary)" stroke="var(--accent-primary)">
                <circle cx="60" cy="50" r="8" stroke="none" />
                <circle cx="440" cy="50" r="8" stroke="none" />
                <path d="M 85 55 C 110 65, 130 15, 160 15 C 180 15, 190 70, 210 70 C 230 70, 250 35, 270 35 C 290 35, 310 65, 340 65 C 370 65, 390 50, 415 50" fill="none" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" />
                <text x="257" y="115" font-family="'Inter', sans-serif" font-weight="700" font-size="34" letter-spacing="16" text-anchor="middle" stroke="none">INTER MUNDOS</text>
              </g>
            </svg>
        </a>;

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    content = content.replace(/<div class="logo">[\s\S]*?<\/div>/, newLogo);
    content = content.replace(/style\.css\?v=\d+/, 'style.css?v=15');
    fs.writeFileSync(file, content);
});
console.log('Logos updated successfully!');
