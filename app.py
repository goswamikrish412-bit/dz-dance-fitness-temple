from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from database import db, ContactSubmission, GalleryImage, Testimonial
from config import Config
import requests
from functools import wraps
import os

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()
    
    # Add default gallery images if none exist
    if GalleryImage.query.count() == 0:
        default_images = [
            {
                'image_url': 'https://customer-assets.emergentagent.com/job_76a138ab-335a-4fc5-86f9-26f3863c0aef/artifacts/32mjl68w_1162.jpg',
                'title': 'Our Spacious Dance Floor',
                'description': 'Professional dance studio with modern facilities'
            },
            {
                'image_url': 'https://customer-assets.emergentagent.com/job_76a138ab-335a-4fc5-86f9-26f3863c0aef/artifacts/f4vguej3_1161.jpg',
                'title': 'Happy Students',
                'description': 'Our amazing dance community'
            },
            {
                'image_url': 'https://customer-assets.emergentagent.com/job_76a138ab-335a-4fc5-86f9-26f3863c0aef/artifacts/t1hbfy8r_1160.jpg',
                'title': 'Group Performance',
                'description': 'Students performing together'
            },
            {
                'image_url': 'https://customer-assets.emergentagent.com/job_76a138ab-335a-4fc5-86f9-26f3863c0aef/artifacts/s5lgz00b_1159.jpg',
                'title': 'Modern Studio',
                'description': 'State-of-the-art dance facilities'
            },
            {
                'image_url': 'https://customer-assets.emergentagent.com/job_76a138ab-335a-4fc5-86f9-26f3863c0aef/artifacts/92771d9j_1158.jpg',
                'title': 'Youth Classes',
                'description': 'Fun and energetic kids classes'
            }
        ]
        for img in default_images:
            gallery_img = GalleryImage(**img)
            db.session.add(gallery_img)
        db.session.commit()
    
    # Add default testimonials if none exist
    if Testimonial.query.count() == 0:
        default_testimonials = [
            {
                'name': 'Priya Sharma',
                'message': 'Amazing instructors and great atmosphere! I\'ve learned so much in just 3 months. The hip hop classes are my favorite!',
                'rating': 5
            },
            {
                'name': 'Rahul Verma',
                'message': 'Best dance studio in Panipat! Professional training, friendly environment, and flexible timings. Highly recommended!',
                'rating': 5
            },
            {
                'name': 'Anita Kumari',
                'message': 'My daughter loves the youth dance classes! She\'s gained so much confidence and made great friends. Thank you DZ Team!',
                'rating': 5
            }
        ]
        for test in default_testimonials:
            testimonial = Testimonial(**test)
            db.session.add(testimonial)
        db.session.commit()

# Admin login decorator
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            flash('Please login to access admin panel', 'error')
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function

# Helper function to fetch images from Unsplash
def get_unsplash_images(query, count=1):
    """Fetch images from Unsplash API"""
    if not app.config['UNSPLASH_ACCESS_KEY']:
        # Return placeholder if no API key
        return [{
            'url': f'https://images.unsplash.com/photo-1518611012118-696072aa579a?w=800&q=80',
            'photographer': 'Unsplash',
            'photographer_url': 'https://unsplash.com'
        }] * count
    
    try:
        url = 'https://api.unsplash.com/search/photos'
        params = {
            'query': query,
            'per_page': count,
            'client_id': app.config['UNSPLASH_ACCESS_KEY']
        }
        response = requests.get(url, params=params, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return [{
                'url': img['urls']['regular'],
                'photographer': img['user']['name'],
                'photographer_url': img['user']['links']['html']
            } for img in data['results']]
    except Exception as e:
        print(f'Error fetching Unsplash images: {e}')
    
    # Fallback to placeholder
    return [{
        'url': f'https://images.unsplash.com/photo-1518611012118-696072aa579a?w=800&q=80',
        'photographer': 'Unsplash',
        'photographer_url': 'https://unsplash.com'
    }] * count

# Routes
@app.route('/')
def index():
    """Home page"""
    testimonials = Testimonial.query.filter_by(is_active=True).limit(3).all()
    gallery_images = GalleryImage.query.filter_by(is_active=True).limit(6).all()
    return render_template('index.html', 
                         testimonials=testimonials,
                         gallery_preview=gallery_images,
                         config=app.config)

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html', config=app.config)

@app.route('/classes')
def classes():
    """Classes page with dynamic images"""
    classes_list = app.config['CLASSES']
    
    # Fetch images for each class
    for class_item in classes_list:
        images = get_unsplash_images(class_item['search_term'], 1)
        class_item['image'] = images[0] if images else None
    
    return render_template('classes.html', 
                         classes=classes_list,
                         config=app.config)

@app.route('/timetable')
def timetable():
    """Timetable page"""
    return render_template('timetable.html', config=app.config)

@app.route('/gallery')
def gallery():
    """Gallery page"""
    gallery_images = GalleryImage.query.filter_by(is_active=True).all()
    return render_template('gallery.html', 
                         gallery_images=gallery_images,
                         config=app.config)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page"""
    if request.method == 'POST':
        try:
            name = request.form.get('name')
            phone = request.form.get('phone')
            message = request.form.get('message')
            
            if not all([name, phone, message]):
                return jsonify({'success': False, 'message': 'All fields are required'}), 400
            
            # Save to database
            submission = ContactSubmission(
                name=name,
                phone=phone,
                message=message
            )
            db.session.add(submission)
            db.session.commit()
            
            return jsonify({
                'success': True,
                'message': 'Thank you! Your message has been received. We will contact you soon.',
                'whatsapp_url': f'https://wa.me/91{app.config["BUSINESS_PHONE"]}?text=Hello! I\'m {name}. {message}'
            })
        except Exception as e:
            return jsonify({'success': False, 'message': 'An error occurred. Please try again.'}), 500
    
    return render_template('contact.html', config=app.config)

# Admin routes
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    """Admin login page"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == app.config['ADMIN_USERNAME'] and password == app.config['ADMIN_PASSWORD']:
            session['admin_logged_in'] = True
            flash('Login successful!', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Invalid credentials', 'error')
    
    return render_template('admin/login.html')

@app.route('/admin/logout')
def admin_logout():
    """Admin logout"""
    session.pop('admin_logged_in', None)
    flash('Logged out successfully', 'success')
    return redirect(url_for('index'))

@app.route('/admin')
@admin_required
def admin_dashboard():
    """Admin dashboard"""
    total_submissions = ContactSubmission.query.count()
    unread_submissions = ContactSubmission.query.filter_by(is_read=False).count()
    total_gallery_images = GalleryImage.query.filter_by(is_active=True).count()
    total_testimonials = Testimonial.query.filter_by(is_active=True).count()
    
    recent_submissions = ContactSubmission.query.order_by(ContactSubmission.submitted_at.desc()).limit(5).all()
    
    return render_template('admin/dashboard.html',
                         total_submissions=total_submissions,
                         unread_submissions=unread_submissions,
                         total_gallery_images=total_gallery_images,
                         total_testimonials=total_testimonials,
                         recent_submissions=recent_submissions)

@app.route('/admin/submissions')
@admin_required
def admin_submissions():
    """View all contact submissions"""
    submissions = ContactSubmission.query.order_by(ContactSubmission.submitted_at.desc()).all()
    return render_template('admin/submissions.html', submissions=submissions)

@app.route('/admin/submissions/<int:id>/read', methods=['POST'])
@admin_required
def mark_submission_read(id):
    """Mark submission as read"""
    submission = ContactSubmission.query.get_or_404(id)
    submission.is_read = True
    db.session.commit()
    return jsonify({'success': True})

@app.route('/admin/submissions/<int:id>/delete', methods=['POST'])
@admin_required
def delete_submission(id):
    """Delete submission"""
    submission = ContactSubmission.query.get_or_404(id)
    db.session.delete(submission)
    db.session.commit()
    flash('Submission deleted successfully', 'success')
    return redirect(url_for('admin_submissions'))

@app.route('/admin/gallery')
@admin_required
def admin_gallery():
    """Manage gallery images"""
    images = GalleryImage.query.order_by(GalleryImage.created_at.desc()).all()
    return render_template('admin/gallery.html', images=images)

@app.route('/admin/gallery/add', methods=['POST'])
@admin_required
def add_gallery_image():
    """Add gallery image"""
    image_url = request.form.get('image_url')
    title = request.form.get('title')
    description = request.form.get('description')
    
    if not image_url:
        flash('Image URL is required', 'error')
        return redirect(url_for('admin_gallery'))
    
    image = GalleryImage(
        image_url=image_url,
        title=title,
        description=description
    )
    db.session.add(image)
    db.session.commit()
    
    flash('Image added successfully', 'success')
    return redirect(url_for('admin_gallery'))

@app.route('/admin/gallery/<int:id>/delete', methods=['POST'])
@admin_required
def delete_gallery_image(id):
    """Delete gallery image"""
    image = GalleryImage.query.get_or_404(id)
    db.session.delete(image)
    db.session.commit()
    flash('Image deleted successfully', 'success')
    return redirect(url_for('admin_gallery'))

@app.route('/admin/testimonials')
@admin_required
def admin_testimonials():
    """Manage testimonials"""
    testimonials = Testimonial.query.order_by(Testimonial.created_at.desc()).all()
    return render_template('admin/testimonials.html', testimonials=testimonials)

@app.route('/admin/testimonials/add', methods=['POST'])
@admin_required
def add_testimonial():
    """Add testimonial"""
    name = request.form.get('name')
    message = request.form.get('message')
    rating = request.form.get('rating', 5, type=int)
    
    if not all([name, message]):
        flash('Name and message are required', 'error')
        return redirect(url_for('admin_testimonials'))
    
    testimonial = Testimonial(
        name=name,
        message=message,
        rating=rating
    )
    db.session.add(testimonial)
    db.session.commit()
    
    flash('Testimonial added successfully', 'success')
    return redirect(url_for('admin_testimonials'))

@app.route('/admin/testimonials/<int:id>/toggle', methods=['POST'])
@admin_required
def toggle_testimonial(id):
    """Toggle testimonial active status"""
    testimonial = Testimonial.query.get_or_404(id)
    testimonial.is_active = not testimonial.is_active
    db.session.commit()
    return jsonify({'success': True, 'is_active': testimonial.is_active})

@app.route('/admin/testimonials/<int:id>/delete', methods=['POST'])
@admin_required
def delete_testimonial(id):
    """Delete testimonial"""
    testimonial = Testimonial.query.get_or_404(id)
    db.session.delete(testimonial)
    db.session.commit()
    flash('Testimonial deleted successfully', 'success')
    return redirect(url_for('admin_testimonials'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port, debug=False)
