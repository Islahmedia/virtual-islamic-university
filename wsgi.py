#!/usr/bin/env python3
"""
WSGI configuration for PythonAnywhere deployment
This file is used by PythonAnywhere to serve your Flask application
"""

import sys
import os
from pathlib import Path

# Add your project directory to Python path
path = '/home/yourusername/mysite'  # Change 'yourusername' to your PythonAnywhere username
if path not in sys.path:
    sys.path.insert(0, path)

# Set up environment variables
os.environ.setdefault('FLASK_ENV', 'production')
os.environ.setdefault('FLASK_DEBUG', 'False')

# Import your Flask app
from app import app, init_db

# Initialize database on startup
try:
    init_db()
    print("Database initialized successfully!")
except Exception as e:
    print(f"Database initialization error: {e}")

# This is what PythonAnywhere will use
application = app

if __name__ == "__main__":
    application.run()
