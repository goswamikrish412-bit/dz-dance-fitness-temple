#!/usr/bin/env python3
"""
Simple HTTP Server for DZ Dance & Fitness Temple Website
"""
import http.server
import socketserver
import os

# Change to the app directory
os.chdir('/app')

# Read port from environment variable, default to 3000 for frontend
PORT = int(os.environ.get('PORT', 3000))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

Handler = MyHTTPRequestHandler

print(f"""
╔═══════════════════════════════════════════════════════════╗
║    DZ Dance & Fitness Temple - Website Server Running     ║
╚═══════════════════════════════════════════════════════════╝

✨ Website is now live at: http://localhost:{PORT}

📄 Available Pages:
   • Home:      http://localhost:{PORT}/index.html
   • About:     http://localhost:{PORT}/about.html
   • Classes:   http://localhost:{PORT}/classes.html
   • Timetable: http://localhost:{PORT}/timetable.html
   • Gallery:   http://localhost:{PORT}/gallery.html
   • Contact:   http://localhost:{PORT}/contact.html

🚀 Features:
   ✅ Fully responsive design
   ✅ WhatsApp integration
   ✅ Contact form
   ✅ Google Maps location
   ✅ Class schedule
   ✅ Pricing plans
   ✅ Gallery with real images

Press CTRL+C to stop the server
""")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n✅ Server stopped successfully!")
        httpd.shutdown()
