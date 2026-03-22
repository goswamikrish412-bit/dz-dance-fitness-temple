// DZ Dance & Fitness Temple - Main JavaScript

// Mobile Menu Toggle
const mobileMenuBtn = document.getElementById('mobileMenuBtn');
const mobileMenu = document.getElementById('mobileMenu');

if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener('click', () => {
        mobileMenu.classList.toggle('hidden');
        const icon = mobileMenuBtn.querySelector('i');
        if (icon) {
            if (mobileMenu.classList.contains('hidden')) {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            } else {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            }
        }
    });
}

// Contact Form Submission
const contactForm = document.getElementById('contactForm');
if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const name = document.getElementById('name').value;
        const phone = document.getElementById('phone').value;
        const message = document.getElementById('message').value;
        
        // Create WhatsApp message
        const whatsappMessage = `Hello! I'm interested in joining DZ Dance & Fitness Temple.\n\nName: ${name}\nPhone: ${phone}\nMessage: ${message}`;
        const whatsappUrl = `https://wa.me/919306926762?text=${encodeURIComponent(whatsappMessage)}`;
        
        // Show success message
        const formMessage = document.getElementById('formMessage');
        if (formMessage) {
            formMessage.classList.remove('hidden');
            formMessage.innerHTML = '<div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded-lg"><strong>Success!</strong> Redirecting you to WhatsApp...</div>';
        }
        
        // Redirect to WhatsApp after 1 second
        setTimeout(() => {
            window.open(whatsappUrl, '_blank');
            contactForm.reset();
        }, 1000);
    });
}

// Smooth Scroll for Anchor Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#' && document.querySelector(href)) {
            e.preventDefault();
            document.querySelector(href).scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});

// Intersection Observer for Fade-in Animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Observe all class cards and sections
document.addEventListener('DOMContentLoaded', () => {
    const animateElements = document.querySelectorAll('.class-card, .gallery-item, .timetable-card');
    animateElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
});

// Navbar Background on Scroll
window.addEventListener('scroll', () => {
    const nav = document.querySelector('nav');
    if (window.scrollY > 100) {
        nav.classList.add('shadow-2xl');
    } else {
        nav.classList.remove('shadow-2xl');
    }
});

// Gallery Lightbox (Simple Implementation)
const galleryImages = document.querySelectorAll('.gallery-item img');
galleryImages.forEach(img => {
    img.addEventListener('click', function() {
        const lightbox = document.createElement('div');
        lightbox.className = 'fixed inset-0 bg-black bg-opacity-90 z-50 flex items-center justify-center p-4';
        lightbox.innerHTML = `
            <div class="relative max-w-6xl w-full">
                <button class="absolute top-4 right-4 text-white text-4xl hover:text-gray-300" onclick="this.parentElement.parentElement.remove()">
                    <i class="fas fa-times"></i>
                </button>
                <img src="${this.src}" alt="${this.alt}" class="w-full h-auto rounded-lg">
            </div>
        `;
        document.body.appendChild(lightbox);
        
        lightbox.addEventListener('click', function(e) {
            if (e.target === lightbox) {
                lightbox.remove();
            }
        });
    });
});

// Pricing Plan Highlight
const pricingCards = document.querySelectorAll('.pricing-card');
pricingCards.forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'scale(1.05)';
    });
    card.addEventListener('mouseleave', function() {
        this.style.transform = 'scale(1)';
    });
});

// Console Log for Debug
console.log('DZ Dance & Fitness Temple - Website Loaded Successfully!');