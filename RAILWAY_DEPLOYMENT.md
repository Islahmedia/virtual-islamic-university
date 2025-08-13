# 🚀 Railway Deployment Guide for Virtual Islamic University

## ✅ Your Project is Ready for Railway!

I've prepared all the necessary files for deploying your Flask application to Railway. Here's what's been configured:

### 📁 **Added Files:**
- `railway.toml` - Railway configuration
- `Procfile` - Process definition 
- `gunicorn.conf.py` - Updated for Railway
- `.env.railway` - Production environment template
- Health check endpoint at `/health`

### 🔧 **Updated Files:**
- `app.py` - Added Railway-compatible configurations
- Added static HTML file serving routes
- Fixed port configuration for Railway

---

## 🚀 **Step-by-Step Deployment:**

### **1. Create Railway Account**
1. Go to [railway.app](https://railway.app)
2. Sign up with GitHub (no credit card required)
3. Verify your email

### **2. Deploy Your Project**
1. **Option A: GitHub Repository (Recommended)**
   - Push your project to GitHub first
   - In Railway, click "New Project" 
   - Choose "Deploy from GitHub repo"
   - Select your repository
   - Railway will auto-detect it's a Python project

2. **Option B: Railway CLI**
   ```bash
   npm install -g @railway/cli
   railway login
   railway init
   railway up
   ```

### **3. Add Environment Variables**
In Railway dashboard, go to your project → Variables tab and add:

```bash
# Required Variables
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=viu-prod-secret-key-2025-secure-random-string-change-this

# Email Configuration  
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USE_SSL=False
MAIL_USERNAME=info.alislahmedia@gmail.com
MAIL_PASSWORD=tlfb fpgz jaig rsrw
ADMIN_EMAIL=info.alislahmedia@gmail.com

# Admin Credentials
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123

# University Info
UNIVERSITY_NAME=Virtual Islamic University
UNIVERSITY_NAME_URDU=ورچوئل اسلامک یونیورسٹی
UNIVERSITY_EMAIL=info@virtualislamicuniversity.com
UNIVERSITY_PHONE=+92-300-1234567

# Railway will auto-set PORT and DATABASE_URL
```

### **4. Add PostgreSQL Database (Free)**
1. In your Railway project, click "New Service"
2. Choose "PostgreSQL" 
3. Railway will automatically set the `DATABASE_URL` environment variable
4. Your app will automatically use PostgreSQL in production

### **5. Deploy!**
- Railway will automatically deploy when you push to GitHub
- Or use `railway deploy` with CLI
- Your app will be available at a URL like: `https://your-app-name.railway.app`

---

## 🎯 **Important Notes:**

### **Database Migration:**
Your app automatically creates tables on first run. The SQLite data from development won't transfer to PostgreSQL, but the structure will be created automatically.

### **Custom Domain (Optional):**
- Railway allows custom domains on free tier
- Go to Settings → Domains in your project

### **Environment Variables Security:**
- Never commit `.env` files to GitHub
- Use Railway's environment variables for production
- Your Gmail app password is already configured

### **Monitoring:**
- Railway provides logs and metrics
- Health check endpoint: `https://your-app.railway.app/health`
- Admin access: `https://your-app.railway.app/admin_login.html`

---

## 🔍 **Testing Your Deployment:**

1. **Main Website:** `https://your-app.railway.app/`
2. **Admin Panel:** `https://your-app.railway.app/admin_login.html`
   - Username: `admin`  
   - Password: `admin123`
3. **Health Check:** `https://your-app.railway.app/health`
4. **API Status:** `https://your-app.railway.app/api`

---

## 🆓 **Railway Free Tier:**
- ✅ **500 hours/month** execution time
- ✅ **No credit card required**
- ✅ **PostgreSQL database included**
- ✅ **Automatic deployments from GitHub**
- ✅ **Custom domain support**
- ✅ **SSL certificates included**

---

## 🛠️ **Troubleshooting:**

### If deployment fails:
1. Check Railway logs in dashboard
2. Ensure all files are committed to GitHub
3. Verify environment variables are set correctly

### If database connection fails:
- Railway sets `DATABASE_URL` automatically
- Check that PostgreSQL service is running
- Your app handles both SQLite (dev) and PostgreSQL (prod)

---

## 📞 **Need Help?**
- Railway has excellent documentation
- Your app includes error handling and logging
- Check the health endpoint for system status

**Your Virtual Islamic University is ready to go live! 🎉**
