#!/usr/bin/env python3
"""Simple HTTP Server for DZ Dance & Fitness Temple Static Website"""
import http.server
import socketserver
import os

os.chdir('/app')
PORT = int(os.environ.get('PORT', 3000))

Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.js': 'application/javascript',
})

print(f"""
╔═══════════════════════════════════════════════════════════╗
║    DZ Dance & Fitness Temple - Static Website Running    ║
╚═══════════════════════════════════════════════════════════╝

✨ Website is live at: http://localhost:{PORT}

📄 Pages Available:
   • Home:      http://localhost:{PORT}/index.html
   • About:     http://localhost:{PORT}/about.html
   • Classes:   http://localhost:{PORT}/classes.html
   • Timetable: http://localhost:{PORT}/timetable.html
   • Gallery:   http://localhost:{PORT}/gallery.html
   • Contact:   http://localhost:{PORT}/contact.html

🎨 Design Features:
   ✅ Modern dark blue/black/gold theme
   ✅ Fully mobile responsive
   ✅ Smooth animations
   ✅ WhatsApp integration
   ✅ Functional contact form
   ✅ Google Maps embedded
   ✅ Gallery with your studio images
   ✅ Dynamic class images from Unsplash

Press CTRL+C to stop
""")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n✅ Server stopped!")
