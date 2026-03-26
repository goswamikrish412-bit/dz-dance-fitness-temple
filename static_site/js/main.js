// DZ Dance & Fitness Temple - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Mobile Navigation Toggle
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (navToggle) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            const icon = this.querySelector('i');
            if (navMenu.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }
    
    // Close mobile menu when clicking a link
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                const icon = navToggle.querySelector('i');
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    });
    
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
    
    // Contact Form Submission
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const submitBtn = this.querySelector('button[type=\"submit\"]');
            const messageDiv = document.getElementById('formMessage');
            
            // Disable submit button
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class=\"fas fa-spinner fa-spin\"></i> Sending...';
            
            try {
                const response = await fetch('/contact', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                
                if (data.success) {
                    messageDiv.className = 'alert alert-success';\n                    messageDiv.innerHTML = `\n                        <i class=\"fas fa-check-circle\"></i> ${data.message}\n                        <br><br>\n                        <a href=\"${data.whatsapp_url}\" target=\"_blank\" class=\"btn btn-whatsapp\">\n                            <i class=\"fab fa-whatsapp\"></i> Continue to WhatsApp\n                        </a>\n                    `;\n                    messageDiv.style.display = 'block';\n                    contactForm.reset();\n                } else {
                    messageDiv.className = 'alert alert-error';\n                    messageDiv.innerHTML = `<i class=\"fas fa-exclamation-circle\"></i> ${data.message}`;\n                    messageDiv.style.display = 'block';\n                }\n            } catch (error) {
                messageDiv.className = 'alert alert-error';\n                messageDiv.innerHTML = '<i class=\"fas fa-exclamation-circle\"></i> An error occurred. Please try again.';\n                messageDiv.style.display = 'block';\n            } finally {
                // Re-enable submit button
                submitBtn.disabled = false;
                submitBtn.innerHTML = '<i class=\"fas fa-paper-plane\"></i> Send Message';\n            }\n        });\n    }\n    \n    // Smooth Scroll for Anchor Links\n    document.querySelectorAll('a[href^=\"#\"]').forEach(anchor => {\n        anchor.addEventListener('click', function (e) {\n            const href = this.getAttribute('href');\n            if (href !== '#' && document.querySelector(href)) {\n                e.preventDefault();\n                document.querySelector(href).scrollIntoView({\n                    behavior: 'smooth'\n                });\n            }\n        });\n    });\n    \n    // Intersection Observer for Fade-in Animations\n    const observerOptions = {\n        threshold: 0.1,\n        rootMargin: '0px 0px -50px 0px'\n    };\n    \n    const observer = new IntersectionObserver((entries) => {\n        entries.forEach(entry => {\n            if (entry.isIntersecting) {\n                entry.target.classList.add('fade-in');\n                observer.unobserve(entry.target);\n            }\n        });\n    }, observerOptions);\n    \n    // Observe all cards and sections\n    document.querySelectorAll('.card, .testimonial-card, .stat-item').forEach(el => {\n        observer.observe(el);\n    });\n    \n    // Gallery Lightbox\n    const galleryItems = document.querySelectorAll('.gallery-item');\n    galleryItems.forEach(item => {\n        item.addEventListener('click', function() {\n            const img = this.querySelector('img');\n            if (!img) return;\n            \n            const lightbox = document.createElement('div');\n            lightbox.className = 'lightbox';\n            lightbox.innerHTML = `\n                <div class=\"lightbox-content\">\n                    <button class=\"lightbox-close\"><i class=\"fas fa-times\"></i></button>\n                    <img src=\"${img.src}\" alt=\"${img.alt}\">\n                    <div class=\"lightbox-caption\">${img.alt}</div>\n                </div>\n            `;\n            document.body.appendChild(lightbox);\n            document.body.style.overflow = 'hidden';\n            \n            // Close lightbox\n            const closeLightbox = () => {\n                lightbox.remove();\n                document.body.style.overflow = '';\n            };\n            \n            lightbox.querySelector('.lightbox-close').addEventListener('click', closeLightbox);\n            lightbox.addEventListener('click', (e) => {\n                if (e.target === lightbox) closeLightbox();\n            });\n        });\n    });\n    \n    // Add active class to current page nav link\n    const currentPage = window.location.pathname.split('/').pop() || 'index';\n    navLinks.forEach(link => {\n        const linkPage = link.getAttribute('href').split('/').pop();\n        if (linkPage === currentPage || (currentPage === '' && linkPage === 'index.html')) {\n            link.classList.add('active');\n        }\n    });\n    \n    console.log('DZ Dance & Fitness Temple - Website Loaded Successfully!');\n});\n\n// Admin Panel Functions\nif (window.location.pathname.includes('/admin')) {\n    // Mark submission as read\n    window.markAsRead = async function(id) {\n        try {\n            const response = await fetch(`/admin/submissions/${id}/read`, {\n                method: 'POST'\n            });\n            const data = await response.json();\n            if (data.success) {\n                location.reload();\n            }\n        } catch (error) {\n            console.error('Error marking as read:', error);\n        }\n    };\n    \n    // Toggle testimonial status\n    window.toggleTestimonial = async function(id) {\n        try {\n            const response = await fetch(`/admin/testimonials/${id}/toggle`, {\n                method: 'POST'\n            });\n            const data = await response.json();\n            if (data.success) {\n                location.reload();\n            }\n        } catch (error) {\n            console.error('Error toggling testimonial:', error);\n        }\n    };\n    \n    // Confirm delete\n    window.confirmDelete = function(message) {\n        return confirm(message || 'Are you sure you want to delete this item?');\n    };\n}
