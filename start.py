#!/usr/bin/env python3
"""
Startup script for Railway deployment
"""
import os
from app import app, init_db

# Initialize database on startup
try:
    init_db()
    print("Database initialized successfully!")
except Exception as e:
    print(f"Database initialization error: {e}")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=False)
