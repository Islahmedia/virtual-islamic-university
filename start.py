#!/usr/bin/env python3
"""
Production startup script for Render.com deployment
"""
import os
from app import app, db

# Ensure the app context is available
with app.app_context():
    # Create all database tables
    db.create_all()
    print("Database tables created successfully!")

if __name__ == "__main__":
    # This will be handled by gunicorn in production
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)
