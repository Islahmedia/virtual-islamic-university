# PythonAnywhere Deployment Guide
# Virtual Islamic University Flask Application

## Prerequisites
1. PythonAnywhere account (free or paid)
2. Your Flask application files ready
3. Gmail account for email functionality

## Step-by-Step Deployment

### 1. Create PythonAnywhere Account
- Go to https://www.pythonanywhere.com
- Sign up for an account
- Choose a plan (free tier is sufficient for testing)

### 2. Upload Your Code

#### Option A: Using Git (Recommended)
1. **Push your code to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. **On PythonAnywhere, open a Bash console and clone:**
   ```bash
   git clone YOUR_GITHUB_REPO_URL mysite
   cd mysite
   ```

#### Option B: Upload Files Directly
1. Create a zip file of your project
2. Upload via PythonAnywhere's file manager
3. Extract in your home directory

### 3. Set Up Virtual Environment
In the PythonAnywhere bash console:
```bash
# Create virtual environment
mkvirtualenv --python=/usr/bin/python3.10 mysite-env

# Activate virtual environment
workon mysite-env

# Navigate to your project
cd ~/mysite

# Install requirements
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create `.env` file in your project directory:
```bash
nano .env
```

Add your configuration (replace with actual values):
```env
# Flask Configuration
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-super-secret-key-here-change-this-12345

# Database Configuration (PythonAnywhere will use SQLite for free accounts)
# For paid accounts, you can use MySQL
DATABASE_URL=sqlite:///instance/university_data.db

# Email Configuration (Gmail)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USE_SSL=False
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-gmail-app-password
ADMIN_EMAIL=your-admin-email@gmail.com

# Admin Login Credentials
ADMIN_USERNAME=admin
ADMIN_PASSWORD=your-secure-admin-password-123

# University Information
UNIVERSITY_NAME=Virtual Islamic University
UNIVERSITY_NAME_URDU=ورچوئل اسلامک یونیورسٹی
UNIVERSITY_EMAIL=info@virtualiu.edu.pk
UNIVERSITY_PHONE=+92-300-1234567

# PythonAnywhere Configuration
PORT=8000
```

### 5. Configure Web App on PythonAnywhere
1. **Go to your PythonAnywhere Dashboard**
2. **Click on "Web" tab**
3. **Click "Add a new web app"**
4. **Choose "Manual configuration" and Python 3.10**
5. **Set the following configurations:**

   - **Source code:** `/home/yourusername/mysite`
   - **Working directory:** `/home/yourusername/mysite`
   - **WSGI configuration file:** `/var/www/yourusername_pythonanywhere_com_wsgi.py`

### 6. Configure WSGI File
Edit the WSGI configuration file:
1. **Go to Web tab → Files → WSGI configuration file**
2. **Replace the content with:**

```python
import sys
import os

# Add your project directory to the sys.path
path = '/home/yourusername/mysite'  # Replace 'yourusername' with your actual username
if path not in sys.path:
    sys.path.insert(0, path)

# Load environment variables
from dotenv import load_dotenv
load_dotenv(os.path.join(path, '.env'))

from app import app, init_db

# Initialize database
try:
    init_db()
    print("Database initialized successfully!")
except Exception as e:
    print(f"Database initialization error: {e}")

application = app
```

### 7. Set Up Static Files (if needed)
In the Web tab, configure static files:
- **URL:** `/assets/`
- **Directory:** `/home/yourusername/mysite/assets/`

- **URL:** `/static/`
- **Directory:** `/home/yourusername/mysite/static/`

### 8. Set Up Virtual Environment
In the Web tab, set the virtualenv path:
```
/home/yourusername/.virtualenvs/mysite-env
```

### 9. Gmail App Password Setup
For email functionality:
1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate an App Password:**
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate password for "Mail"
   - Use this password in your `.env` file

### 10. Database Setup
For free accounts (SQLite):
```bash
# Create instance directory
mkdir -p ~/mysite/instance

# The database will be created automatically when the app runs
```

For paid accounts (MySQL):
1. Create a MySQL database in the Databases tab
2. Update DATABASE_URL in .env file
3. Install MySQL adapter: `pip install mysqlclient`

### 11. Test Your Application
1. **Click "Reload" in the Web tab**
2. **Visit your site:** `https://yourusername.pythonanywhere.com`
3. **Check error logs** if something doesn't work

### 12. Domain Configuration (Optional)
For custom domain:
1. **Upgrade to paid account**
2. **Configure DNS settings**
3. **Add domain in Web tab**

## Troubleshooting

### Common Issues:

1. **Import errors:**
   - Check virtual environment is activated
   - Verify all packages are installed: `pip list`

2. **Database errors:**
   - Ensure instance directory exists
   - Check file permissions

3. **Static files not loading:**
   - Configure static file mappings in Web tab
   - Check file paths

4. **Email not working:**
   - Verify Gmail app password
   - Check firewall/port restrictions

### Useful Commands:
```bash
# Check logs
tail -f /var/log/yourusername.pythonanywhere.com.error.log
tail -f /var/log/yourusername.pythonanywhere.com.server.log

# Restart web app (alternative to reload button)
touch /var/www/yourusername_pythonanywhere_com_wsgi.py

# Test your app locally
python app.py
```

## Security Notes:
1. **Change default admin password**
2. **Use strong SECRET_KEY**
3. **Don't commit .env file to git**
4. **Regularly update dependencies**
5. **Monitor access logs**

## Features Available After Deployment:
- ✅ Main university website
- ✅ Course pages
- ✅ Admission form
- ✅ Contact form
- ✅ Admin dashboard
- ✅ Email notifications
- ✅ Database management
- ✅ Session management
- ✅ Urdu/Arabic content support

Your Virtual Islamic University website will be live at:
`https://yourusername.pythonanywhere.com`

## Post-Deployment:
1. **Test all functionality**
2. **Set up regular backups**
3. **Monitor performance**
4. **Update content as needed**
5. **Consider SEO optimization**

Good luck with your deployment! 🚀
