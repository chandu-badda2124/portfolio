// Add smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Add glow effect on hover
const buttons = document.querySelectorAll('.glow-button');
buttons.forEach(button => {
    button.addEventListener('mouseover', () => {
        button.style.boxShadow = '0 0 10px #00ffcc, 0 0 20px #00ffcc, 0 0 40px #00ffcc';
    });
    button.addEventListener('mouseout', () => {
        button.style.boxShadow = 'none';
    });
});