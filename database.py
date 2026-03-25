from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class ContactSubmission(db.Model):
    """Contact form submissions"""
    __tablename__ = 'contact_submissions'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    message = db.Column(db.Text, nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_read = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<ContactSubmission {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'message': self.message,
            'submitted_at': self.submitted_at.strftime('%Y-%m-%d %H:%M:%S'),
            'is_read': self.is_read
        }

class GalleryImage(db.Model):
    """Gallery images"""
    __tablename__ = 'gallery_images'
    
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(500), nullable=False)
    title = db.Column(db.String(200))
    description = db.Column(db.Text)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<GalleryImage {self.title}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'image_url': self.image_url,
            'title': self.title,
            'description': self.description,
            'is_active': self.is_active
        }

class Testimonial(db.Model):
    """Student testimonials"""
    __tablename__ = 'testimonials'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, default=5)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Testimonial {self.name}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'message': self.message,
            'rating': self.rating,
            'is_active': self.is_active
        }