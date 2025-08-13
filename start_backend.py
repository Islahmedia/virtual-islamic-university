#!/usr/bin/env python3
"""
Virtual Islamic University Backend Startup Script
This script initializes and starts the Flask backend server
"""

import os
import sys
from app import app, db

def check_environment():
    """Check if all required environment variables are set"""
    required_vars = [
        'MAIL_USERNAME',
        'MAIL_PASSWORD',
        'ADMIN_EMAIL'
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\n📝 Please update your .env file with the required values")
        print("   Example .env file has been created for you")
        return False
    
    return True

def initialize_database():
    """Initialize the database with tables"""
    try:
        with app.app_context():
            # Create all tables
            db.create_all()
            print("✅ Database initialized successfully")
            
            # Check if tables exist
            from sqlalchemy import inspect
            inspector = inspect(db.engine)
            tables = inspector.get_table_names()
            
            print(f"📊 Database tables: {', '.join(tables)}")
            
            return True
    except Exception as e:
        print(f"❌ Database initialization failed: {e}")
        return False

def print_startup_info():
    """Print startup information"""
    print("\n" + "="*60)
    print("🕌 Virtual Islamic University - Backend Server")
    print("="*60)
    print(f"🌐 Server URL: http://localhost:5000")
    print(f"📡 API Base URL: http://localhost:5000/api")
    print(f"📧 Admin Email: {os.getenv('ADMIN_EMAIL', 'Not configured')}")
    print(f"🗄️ Database: {os.getenv('DATABASE_URL', 'sqlite:///university_data.db')}")
    print("="*60)
    print("\n📋 Available API Endpoints:")
    print("   • POST /api/submit-contact     - Contact form submission")
    print("   • POST /api/submit-admission   - Admission form submission")
    print("   • GET  /api/admin/applications - View applications (Admin)")
    print("   • GET  /api/admin/contacts     - View contacts (Admin)")
    print("   • GET  /api/admin/stats        - View statistics (Admin)")
    print("\n💡 Tips:")
    print("   • Update your HTML forms to use: http://localhost:5000/api")
    print("   • Include the form-handler.js script in your HTML files")
    print("   • Configure email settings in .env file for notifications")
    print("\n🚀 Server starting...")
    print("   Press Ctrl+C to stop the server")
    print("="*60 + "\n")

def main():
    """Main startup function"""
    print("🔧 Checking environment...")
    
    # Check environment variables
    if not check_environment():
        sys.exit(1)
    
    print("✅ Environment check passed")
    
    # Initialize database
    print("🗄️ Initializing database...")
    if not initialize_database():
        sys.exit(1)
    
    # Print startup information
    print_startup_info()
    
    # Start the server
    try:
        app.run(
            debug=os.getenv('FLASK_DEBUG', 'True').lower() == 'true',
            host='0.0.0.0',
            port=int(os.getenv('PORT', 5000)),
            use_reloader=False  # Disable reloader to avoid double startup messages
        )
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped by user")
        print("👋 Thank you for using Virtual Islamic University Backend!")
    except Exception as e:
        print(f"\n❌ Server error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
