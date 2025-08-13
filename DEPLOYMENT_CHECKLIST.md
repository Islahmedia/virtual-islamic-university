# PythonAnywhere Deployment Checklist ✅
## Virtual Islamic University Flask Application

### Pre-Deployment
- [ ] PythonAnywhere account created
- [ ] Gmail account ready for email functionality
- [ ] Project files organized and ready

### File Preparation
- [ ] `wsgi.py` file created ✅
- [ ] `requirements-pythonanywhere.txt` ready ✅
- [ ] Deployment guide reviewed ✅
- [ ] Environment variables list prepared

### Account Setup
- [ ] Logged into PythonAnywhere
- [ ] Bash console opened
- [ ] Virtual environment created
- [ ] Project files uploaded (Git or direct upload)

### Environment Configuration
- [ ] Virtual environment activated
- [ ] Requirements installed: `pip install -r requirements-pythonanywhere.txt`
- [ ] `.env` file created with actual values
- [ ] Database directory created: `mkdir -p ~/mysite/instance`

### Web App Configuration
- [ ] Web app created (Manual configuration, Python 3.10)
- [ ] Source code path set: `/home/yourusername/mysite`
- [ ] Working directory set: `/home/yourusername/mysite`
- [ ] Virtual environment path set: `/home/yourusername/.virtualenvs/mysite-env`
- [ ] WSGI file configured with your code

### Static Files Setup
- [ ] Assets mapping: `/assets/` → `/home/yourusername/mysite/assets/`
- [ ] Static mapping: `/static/` → `/home/yourusername/mysite/static/`

### Email Setup
- [ ] Gmail 2FA enabled
- [ ] App password generated
- [ ] App password added to `.env` file

### Testing
- [ ] Web app reloaded
- [ ] Website loads: `https://yourusername.pythonanywhere.com`
- [ ] Contact form works
- [ ] Admission form works
- [ ] Admin login works
- [ ] Email notifications work

### Security
- [ ] Admin password changed from default
- [ ] Strong SECRET_KEY set
- [ ] `.env` file not committed to Git

### Post-Deployment
- [ ] All pages tested
- [ ] Forms tested
- [ ] Admin dashboard tested
- [ ] Database working
- [ ] Email sending working
- [ ] Error logs checked

## Quick Commands Reference

### Create Virtual Environment:
```bash
mkvirtualenv --python=/usr/bin/python3.10 mysite-env
workon mysite-env
```

### Install Requirements:
```bash
pip install -r requirements-pythonanywhere.txt
```

### Check Logs:
```bash
tail -f /var/log/yourusername.pythonanywhere.com.error.log
```

### Restart App:
- Use "Reload" button in Web tab
- Or: `touch /var/www/yourusername_pythonanywhere_com_wsgi.py`

## Your App Features:
✅ Multi-language support (Urdu/Arabic/English)
✅ Course management
✅ Student admission system
✅ Contact form with email notifications
✅ Admin dashboard with authentication
✅ Session management
✅ Database integration
✅ Mobile-responsive design

## Success! 🎉
Your Virtual Islamic University website will be live at:
**`https://yourusername.pythonanywhere.com`**

Replace `yourusername` with your actual PythonAnywhere username.
