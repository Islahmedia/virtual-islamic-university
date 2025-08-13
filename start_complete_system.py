#!/usr/bin/env python3
"""
Complete system startup script for Virtual Islamic University
This script starts both the Flask backend API and the frontend HTTP server
"""
import subprocess
import sys
import time
import os
import threading
import webbrowser
from pathlib import Path

def start_flask_backend():
    """Start the Flask backend server"""
    print("🚀 Starting Flask Backend API Server...")
    try:
        # Start Flask app
        result = subprocess.run([
            sys.executable, "app.py"
        ], cwd=os.getcwd(), capture_output=False, text=True)
    except Exception as e:
        print(f"❌ Error starting Flask backend: {e}")

def start_frontend_server():
    """Start the frontend HTTP server"""
    print("🌐 Starting Frontend HTTP Server...")
    try:
        result = subprocess.run([
            sys.executable, "serve_frontend.py"
        ], cwd=os.getcwd(), capture_output=False, text=True)
    except Exception as e:
        print(f"❌ Error starting frontend server: {e}")

def check_requirements():
    """Check if all required files exist"""
    required_files = [
        "app.py",
        "admission.html",
        "serve_frontend.py"
    ]
    
    missing_files = []
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   • {file}")
        return False
    
    return True

def main():
    """Main startup function"""
    print("🕌 Virtual Islamic University - Complete System Startup")
    print("=" * 60)
    print()
    
    # Check requirements
    if not check_requirements():
        print("\n❌ Cannot start system - missing required files")
        return
    
    print("📋 Starting System Components:")
    print("   1. Flask Backend API (Port 5000)")
    print("   2. Frontend HTTP Server (Port 8080)")
    print()
    
    # Start backend in a separate thread
    print("🔧 Starting Flask Backend...")
    backend_thread = threading.Thread(target=start_flask_backend, daemon=True)
    backend_thread.start()
    
    # Wait a moment for backend to start
    time.sleep(3)
    
    # Start frontend in a separate thread
    print("🔧 Starting Frontend Server...")
    frontend_thread = threading.Thread(target=start_frontend_server, daemon=True)
    frontend_thread.start()
    
    # Wait a moment for frontend to start
    time.sleep(2)
    
    print("\n✅ System Started Successfully!")
    print("=" * 60)
    print("🌐 Access URLs:")
    print("   • Frontend: http://localhost:8080")
    print("   • Admission Form: http://localhost:8080/admission.html")
    print("   • Backend API: http://localhost:5000")
    print("=" * 60)
    print()
    
    # Auto-open browser
    try:
        print("🌍 Opening admission form in browser...")
        webbrowser.open('http://localhost:8080/admission.html')
    except Exception as e:
        print(f"⚠️  Could not auto-open browser: {e}")
        print("   Please manually open: http://localhost:8080/admission.html")
    
    print("\n💡 Tips:")
    print("   • Fill out the admission form and submit it")
    print("   • You should now see success notifications!")
    print("   • Press Ctrl+C to stop all servers")
    print()
    
    try:
        # Keep the main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down all servers...")
        print("👋 Thank you for using Virtual Islamic University!")

if __name__ == '__main__':
    main()
