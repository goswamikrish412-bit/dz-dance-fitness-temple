# DZ Dance & Fitness Temple - Dynamic Website

A fully functional, production-ready dynamic website built with Flask backend and modern UI design.

## 🎯 Features Implemented

### ✅ **Fully Dynamic Website**
- Python Flask backend with SQLAlchemy ORM
- SQLite database (no complex setup required)
- Dynamic content management via admin panel
- RESTful API endpoints

### ✅ **Removed Pricing Sections**
- All paid plans, pricing, and subscription content completely removed
- Clean, professional layout without any payment references

### ✅ **Modern UI Design**
- Premium color scheme: Dark Blue (#0A1929), Black, White, Gold accents
- Professional, high-end design for fitness/dance industry
- Smooth animations and transitions
- Fully mobile responsive
- Fast loading and optimized

### ✅ **Functional Features**
- **Contact Form**: Stores submissions in database + WhatsApp integration
- **Gallery Management**: Admin can add/remove gallery images
- **Testimonial Management**: Admin can add/edit testimonials
- **Dynamic Class Images**: Fetches from Unsplash API (configurable)
- **Admin Panel**: Full content management system

### ✅ **Pages Created**
1. **Home** - Hero, stats, gallery preview, classes, testimonials, CTAs
2. **About Us** - Studio story, mission, vision
3. **Classes** - All 9 classes with dynamic images from Unsplash
4. **Timetable** - Weekly class schedule
5. **Gallery** - Image gallery with management
6. **Contact** - Functional form + Google Maps
7. **Admin Panel** - Dashboard, submissions, gallery, testimonials

## 📁 Project Structure

```
/app/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── database.py           # Database models
├── requirements.txt      # Python dependencies
├── dz_dance.db          # SQLite database (auto-created)
├── static/
│   ├── css/
│   │   └── style.css    # Modern CSS with dark theme
│   ├── js/
│   │   └── main.js      # JavaScript functionality
│   └── images/          # Static images (if any)
└── templates/           # HTML templates
    ├── layout.html      # Base template
    ├── index.html       # Home page
    ├── about.html       # About page
    ├── classes.html     # Classes with dynamic images
    ├── timetable.html   # Schedule
    ├── gallery.html     # Gallery
    ├── contact.html     # Contact form
    └── admin/           # Admin panel templates
        ├── login.html
        ├── dashboard.html
        ├── submissions.html
        ├── gallery.html
        └── testimonials.html
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation & Setup

1. **Install Dependencies**
```bash
cd /app
pip install -r requirements.txt
```

2. **Run the Application**
```bash
python3 app.py
```

The website will be available at: `http://localhost:3000`

### For Production Deployment

The application is configured to work on any hosting platform:

```bash
# Set environment variables (optional)
export PORT=3000
export SECRET_KEY=your-secret-key-here
export ADMIN_USERNAME=admin
export ADMIN_PASSWORD=your-secure-password

# Run the app
python3 app.py
```

## 🎨 Design Features

### Color Scheme
- **Primary Dark**: #0A1929
- **Primary Blue**: #1A2332
- **Secondary Blue**: #1e3a5f
- **Accent Gold**: #D4AF37
- **White**: #FFFFFF
- **Black**: #000000

### Typography
- Modern sans-serif fonts (Inter, Segoe UI)
- Responsive font sizing with clamp()
- Clear hierarchy and readability

### Animations
- Smooth transitions (0.3s ease-in-out)
- Fade-in animations on scroll
- Hover effects on cards and buttons
- Pulse animation for WhatsApp button

## 📱 Mobile Responsive

- Fully responsive design
- Mobile-first approach
- Touch-friendly navigation
- Optimized for all screen sizes

## 🔧 Configuration

### Admin Panel Access
**Default Credentials:**
- URL: `http://localhost:3000/admin/login`
- Username: `admin`
- Password: `admin123`

**⚠️ IMPORTANT:** Change these credentials immediately in production!

Edit `/app/config.py`:
```python
ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'your-username')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'your-secure-password')
```

### Unsplash API Integration

To enable dynamic images for classes page:

1. Get free API key from: https://unsplash.com/developers
2. Set environment variable:
```bash
export UNSPLASH_ACCESS_KEY=your-unsplash-key-here
```

Or edit `/app/config.py`:
```python
UNSPLASH_ACCESS_KEY = 'your-key-here'
```

**Note:** If no API key is provided, placeholder images will be used.

### Business Information

Edit `/app/config.py` to update:
- Business name
- Phone number
- Address
- Opening hours
- Class information

## 📊 Database

### SQLite Database
- Location: `/app/dz_dance.db`
- Auto-created on first run
- No configuration needed
- Contains:
  - Contact submissions
  - Gallery images
  - Testimonials

### Database Models
1. **ContactSubmission**: Stores contact form data
2. **GalleryImage**: Manages gallery photos
3. **Testimonial**: Stores customer reviews

## 🎯 Admin Panel Features

### Dashboard
- Total submissions count
- Unread submissions count
- Gallery images count
- Testimonials count
- Recent submissions preview

### Contact Submissions
- View all form submissions
- Mark as read/unread
- Delete submissions
- Contact information display

### Gallery Management
- Add new images (via URL)
- Add titles and descriptions
- Delete images
- Active/inactive status

### Testimonials Management
- Add new testimonials
- Edit existing ones
- Activate/deactivate
- Delete testimonials
- Star rating system

## 📱 Contact Form

### Features
- Stores data in database
- Real-time validation
- Success/error messages
- WhatsApp integration
- Email-ready (extendable)

### Form Fields
- Name (required)
- Phone (required)
- Message (required)

### Submission Flow
1. User fills form
2. Data validated
3. Saved to database
4. Success message shown
5. Option to continue to WhatsApp

## 🌐 Deployment

### Universal Hosting Support

This website works on:
- **Shared Hosting** (with Python support)
- **VPS** (Ubuntu, CentOS, etc.)
- **Cloud Platforms** (AWS, Google Cloud, Azure)
- **PaaS** (Heroku, Railway, Render)
- **Local Server**

### Deployment Steps

1. **Upload files** to your server
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Set environment variables** (optional)
4. **Run application**: `python3 app.py`

### Using Gunicorn (Production)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:3000 app:app
```

### Using Supervisor (Auto-restart)

Already configured! Check `/etc/supervisor/conf.d/supervisord.conf`

```bash
sudo supervisorctl restart frontend
sudo supervisorctl status
```

## 🔒 Security

### Recommendations
1. Change admin credentials immediately
2. Use strong SECRET_KEY in production
3. Enable HTTPS
4. Regular database backups
5. Keep dependencies updated

### Environment Variables
```bash
SECRET_KEY=random-secret-key-here
ADMIN_USERNAME=your-admin-username
ADMIN_PASSWORD=strong-password-here
UNSPLASH_ACCESS_KEY=your-api-key
```

## 📞 Contact Integration

### WhatsApp
- Floating button on all pages
- Direct message links
- Contact form integration
- Phone: 9306926762

### Google Maps
- Embedded map on contact page
- Location: Model Town, Panipat, Haryana

## 🎓 Classes Offered

1. Hip Hop Classes
2. Zumba Classes
3. Contemporary Dance
4. Choreography Classes
5. Youth Dance Classes (Ages 5-15)
6. Beginner Dance Classes
7. Advanced Dance Classes
8. Intermediate Classes
9. Private Lessons

## 📅 Opening Hours

- **Monday - Saturday**: 6:00 AM – 10:00 PM
- **Sunday**: 9:00 AM – 5:00 PM

## 🛠️ Troubleshooting

### App not starting?
```bash
# Check logs
tail -f /var/log/supervisor/frontend.err.log

# Verify Python version
python3 --version

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Database issues?
```bash
# Delete and recreate database
rm /app/dz_dance.db
python3 app.py  # Will auto-create new database
```

### Port already in use?
```bash
# Change port in config or environment
export PORT=8080
python3 app.py
```

## 📝 Maintenance

### Database Backup
```bash
cp /app/dz_dance.db /app/backup_$(date +%Y%m%d).db
```

### Update Content
- Login to admin panel
- Manage gallery, testimonials, submissions
- All changes reflected immediately

### Add New Classes
Edit `/app/config.py` - `CLASSES` list

## 🎉 What's Different from Static Site?

### Before (Static):
- ❌ No backend functionality
- ❌ No database
- ❌ Contact form didn't work
- ❌ No admin panel
- ❌ Manual content updates
- ❌ Hardcoded content

### After (Dynamic):
- ✅ Full Flask backend
- ✅ SQLite database
- ✅ Functional contact form with storage
- ✅ Complete admin panel
- ✅ Easy content management
- ✅ Dynamic content loading
- ✅ Unsplash API integration
- ✅ No pricing sections
- ✅ Modern premium design
- ✅ Production-ready

## 📧 Support

For questions or support:
- Phone: 9306926762
- WhatsApp: https://wa.me/919306926762

## 📄 License

© 2025 DZ Dance & Fitness Temple. All rights reserved.

---

**Built with ❤️ using Flask, SQLAlchemy, and modern web technologies.**
