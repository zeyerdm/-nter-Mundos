document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.service-card');

    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            // Apply a subtle dynamic radial gradient on hover tracking mouse
            card.style.background = `radial-gradient(800px circle at ${x}px ${y}px, rgba(255,255,255,0.06), transparent 40%), rgba(15, 23, 42, 0.4)`;
        });

        card.addEventListener('mouseleave', () => {
            // Reset background when mouse leaves
            card.style.background = `rgba(15, 23, 42, 0.4)`;
        });
    });

    // Mobile Menu Toggle
    const mobileBtn = document.querySelector('.mobile-menu-btn');
    const navbar = document.querySelector('.navbar');
    
    if (mobileBtn && navbar) {
        mobileBtn.addEventListener('click', () => {
            navbar.classList.toggle('active');
            const icon = mobileBtn.querySelector('i');
            if (navbar.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-xmark');
            } else {
                icon.classList.remove('fa-xmark');
                icon.classList.add('fa-bars');
            }
        });
    }

    // Scroll Reveal Animation
    const reveals = document.querySelectorAll('.reveal');
    const revealOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const revealOnScroll = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            } else {
                entry.target.classList.remove('active'); // Re-animate every time
            }
        });
    }, revealOptions);

    reveals.forEach(reveal => {
        revealOnScroll.observe(reveal);
    });
});
