import os

class Config:
    """Application configuration"""
    
    # Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///dz_dance.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Unsplash API configuration (Get free key from https://unsplash.com/developers)
    UNSPLASH_ACCESS_KEY = os.environ.get('UNSPLASH_ACCESS_KEY', '')
    
    # Business Information
    BUSINESS_NAME = 'DZ Dance & Fitness Temple'
    BUSINESS_PHONE = '9306926762'
    BUSINESS_ADDRESS = '476, R, Near Bal Vikas School, Model Town, Panipat, Haryana, 132103'
    
    # Opening Hours
    OPENING_HOURS = {
        'weekdays': 'Monday - Saturday: 6:00 AM – 10:00 PM',
        'weekend': 'Sunday: 9:00 AM – 5:00 PM'
    }
    
    # Admin credentials (change these!)
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin123')
    
    # Classes configuration
    CLASSES = [
        {
            'id': 1,
            'name': 'Hip Hop Classes',
            'description': 'Master urban dance moves with high-energy hip hop choreography. Learn breaking, popping, locking, and freestyle techniques.',
            'level': 'All Levels',
            'duration': '60 minutes',
            'icon': 'fa-music',
            'search_term': 'hip hop dance'
        },
        {
            'id': 2,
            'name': 'Zumba Classes',
            'description': 'High-energy Latin-inspired dance fitness workout. Burn calories, lose weight, and have fun while dancing!',
            'level': 'All Levels',
            'duration': '60 minutes',
            'icon': 'fa-heart',
            'search_term': 'zumba fitness'
        },
        {
            'id': 3,
            'name': 'Contemporary Dance',
            'description': 'Express yourself through fluid, graceful movements. Combines elements of ballet, jazz, and modern dance.',
            'level': 'Intermediate to Advanced',
            'duration': '60 minutes',
            'icon': 'fa-star',
            'search_term': 'contemporary dance'
        },
        {
            'id': 4,
            'name': 'Choreography Classes',
            'description': 'Learn professional choreography for performances, competitions, and special events.',
            'level': 'Intermediate to Advanced',
            'duration': '60 minutes',
            'icon': 'fa-trophy',
            'search_term': 'dance choreography'
        },
        {
            'id': 5,
            'name': 'Youth Dance Classes',
            'description': 'Specially designed for kids aged 5-15. Fun, energetic classes that build confidence, coordination, and creativity.',
            'level': 'Kids (5-15 years)',
            'duration': '45 minutes',
            'icon': 'fa-child',
            'search_term': 'kids dance'
        },
        {
            'id': 6,
            'name': 'Beginner Dance Classes',
            'description': 'Perfect for those just starting their dance journey. Learn basic steps, rhythm, coordination, and build your confidence.',
            'level': 'Beginner',
            'duration': '45 minutes',
            'icon': 'fa-seedling',
            'search_term': 'beginner dance'
        },
        {
            'id': 7,
            'name': 'Advanced Dance Classes',
            'description': 'Take your dancing to the next level with advanced techniques, complex routines, and performance-ready choreography.',
            'level': 'Advanced',
            'duration': '75 minutes',
            'icon': 'fa-star',
            'search_term': 'advanced dance'
        },
        {
            'id': 8,
            'name': 'Intermediate Classes',
            'description': 'Build upon your foundation with more complex moves, styling, and performance techniques.',
            'level': 'Intermediate',
            'duration': '60 minutes',
            'icon': 'fa-fire',
            'search_term': 'dance workout'
        },
        {
            'id': 9,
            'name': 'Private Lessons',
            'description': 'One-on-one personalized training tailored to your goals. Get undivided attention and accelerated progress.',
            'level': 'Customized',
            'duration': 'Flexible',
            'icon': 'fa-user',
            'search_term': 'personal dance training'
        }
    ]