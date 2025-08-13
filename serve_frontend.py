#!/usr/bin/env python3
"""
Simple HTTP server to serve the frontend HTML files
This avoids CORS issues when the form submits to the Flask API
"""
import http.server
import socketserver
import os
import webbrowser
import threading
import time

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve files with proper MIME types"""
    
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_OPTIONS(self):
        """Handle preflight OPTIONS requests"""
        self.send_response(200)
        self.end_headers()

def start_server():
    """Start the HTTP server"""
    PORT = 8080
    
    # Change to the directory containing HTML files
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    Handler = CustomHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("=" * 60)
            print("🌐 Frontend Server Started")
            print("=" * 60)
            print(f"📍 Server URL: http://localhost:{PORT}")
            print(f"📄 Admission Form: http://localhost:{PORT}/admission.html")
            print(f"🏠 Home Page: http://localhost:{PORT}/index.html")
            print("=" * 60)
            print("💡 Tips:")
            print("   • Make sure Flask API server is running on port 5000")
            print("   • Open the admission form in your browser using the URL above")
            print("   • This server serves static files and avoids CORS issues")
            print("=" * 60)
            print("🚀 Server is running... Press Ctrl+C to stop")
            print()
            
            # Auto-open browser after a short delay
            def open_browser():
                time.sleep(2)
                webbrowser.open(f'http://localhost:{PORT}/admission.html')
            
            browser_thread = threading.Thread(target=open_browser)
            browser_thread.daemon = True
            browser_thread.start()
            
            httpd.serve_forever()
            
    except OSError as e:
        if e.errno == 10048:  # Port already in use
            print(f"❌ Port {PORT} is already in use!")
            print(f"   Please stop any existing server on port {PORT} or use a different port")
        else:
            print(f"❌ Server error: {e}")
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
        print("👋 Frontend server shutdown complete!")

if __name__ == '__main__':
    start_server()
