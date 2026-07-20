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
});
