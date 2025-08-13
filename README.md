# Virtual Islamic University Website 🕌📚

A comprehensive Islamic educational platform built with Flask and modern web technologies, offering online courses in Quranic studies, Arabic language, and Islamic sciences.

## Features

### 🎓 Educational Features
- **Course Management**: Multiple Islamic courses including Quran, Arabic, and Islamic Studies
- **Admission System**: Complete online admission process with application tracking
- **Course Details**: Detailed course information with multimedia content
- **Faculty Profiles**: Information about experienced Islamic scholars and teachers

### 🛠️ Technical Features
- **Responsive Design**: Mobile-first approach with Bootstrap RTL support
- **Admin Dashboard**: Comprehensive admin panel for managing applications and contacts
- **Email Integration**: Automated email notifications for admissions and contact forms
- **Database Management**: SQLAlchemy ORM with PostgreSQL support for production
- **Authentication System**: Secure admin authentication with session management
- **Multilingual Support**: Arabic and Urdu language support with proper fonts

## Technology Stack

### Backend
- **Flask**: Python web framework
- **SQLAlchemy**: Database ORM
- **PostgreSQL**: Production database
- **Flask-Mail**: Email functionality
- **Gunicorn**: Production WSGI server

### Frontend
- **HTML5/CSS3**: Modern web standards
- **Bootstrap 5**: Responsive framework with RTL support
- **JavaScript**: Interactive functionality
- **AOS**: Animation on scroll effects
- **Custom Arabic/Urdu fonts**: Mehr Nastaliq and Noto fonts

## Installation

### Prerequisites
- Python 3.8+
- PostgreSQL (for production)
- Git

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/virtual-islamic-university.git
cd virtual-islamic-university
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Initialize database:
```bash
python app.py
```

6. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:10000`

## Deployment

This application is configured for deployment on:
- **Render.com** (Recommended)
- **Heroku**
- **Railway**
- Any platform supporting Python/Flask

### Environment Variables

Set the following environment variables in your hosting platform:

```env
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://...
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
ADMIN_USERNAME=admin
ADMIN_PASSWORD=secure-password
```

## Course Offerings

### 📖 Quranic Studies (فہم القرآن)
- Quranic recitation and Tajweed
- Tafseer and interpretation
- Quranic Arabic

### 🔤 Arabic Language (اللغة العربية)
- Classical Arabic grammar
- Modern Standard Arabic
- Arabic literature

### 🕌 Islamic Studies (علوم الدین)
- Islamic theology (Aqeedah)
- Islamic jurisprudence (Fiqh)
- Hadith studies
- Islamic history

## Admin Panel

Access the admin panel at `/admin_login.html` to:
- View and manage admission applications
- Respond to contact form submissions
- View statistics and analytics
- Approve/reject applications

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Email**: info.alislahmedia@gmail.com
- **Website**: [Virtual Islamic University](https://your-domain.com)
- **Phone**: +92-300-1234567

## Acknowledgments

- Islamic scholars and educators who contributed to course content
- Open source community for the tools and libraries used
- Students and users who provide feedback and suggestions

---

**بارک اللہ فیکم** - May Allah bless you all

A complete web application for Virtual Islamic University with course management, admission system, contact forms, and admin dashboard.

## 🚀 Live Demo

- **Website**: [Your deployed URL will be here]
- **Admin Panel**: [Your deployed URL]/admin_login.html

## ✨ Features

- **Multi-language support**: Arabic, Urdu, and English
- **Course Management**: Islamic Studies, Arabic, Quran courses
- **Admission System**: Online application with email notifications
- **Contact Forms**: Direct communication with admin
- **Admin Dashboard**: Manage applications, contacts, and statistics
- **Email Integration**: Automatic notifications via Gmail
- **Responsive Design**: Works on all devices

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Database**: PostgreSQL (production), SQLite (development)
- **Frontend**: HTML5, CSS3, JavaScript
- **Email**: Flask-Mail with Gmail SMTP
- **Hosting**: Render.com

## 📋 Local Development Setup

1. **Clone the repository**
   ```bash
   git clone [your-repo-url]
   cd "Web project"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your actual values
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Website: http://localhost:5000
   - Admin: http://localhost:5000/admin_login.html

## 🌐 Production Deployment (Render.com)

### Prerequisites
- GitHub account
- Gmail account with App Password enabled
- Render.com account (free)

### Step 1: Prepare Your Gmail
1. Enable 2-Factor Authentication on Gmail
2. Generate App Password:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate password for "Mail"
   - Save this password for later

### Step 2: Upload to GitHub
1. Create new repository on GitHub
2. Upload all project files (excluding .env file)

### Step 3: Deploy on Render.com
1. **Create Web Service**
   - Connect your GitHub repository
   - Choose "Web Service"
   - Runtime: Python 3
   - Build Command: `./build.sh`
   - Start Command: `gunicorn app:app`

2. **Set Environment Variables**
   ```
   FLASK_ENV=production
   FLASK_DEBUG=False
   SECRET_KEY=[generate-strong-secret-key]
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=[your-gmail]
   MAIL_PASSWORD=[your-gmail-app-password]
   ADMIN_EMAIL=[your-admin-email]
   ADMIN_USERNAME=admin
   ADMIN_PASSWORD=[secure-admin-password]
   UNIVERSITY_EMAIL=[your-university-email]
   UNIVERSITY_PHONE=+92-300-1234567
   ```

3. **Add PostgreSQL Database**
   - Create PostgreSQL database on Render
   - Copy the DATABASE_URL to your environment variables

## 🔧 Configuration

### Email Settings
- Uses Gmail SMTP for sending emails
- Requires Gmail App Password (not regular password)
- Automatic notifications for contact forms and admissions

### Admin Access
- Default username: admin
- Change password in environment variables
- Access via: /admin_login.html

### Database
- Development: SQLite (automatic)
- Production: PostgreSQL (Render.com provides automatically)

## 📱 Usage

### For Visitors
1. **Browse Courses**: View available Islamic courses
2. **Apply for Admission**: Fill online application form
3. **Contact**: Send messages via contact form
4. **Faculty**: View teacher profiles

### For Administrators
1. **Login**: Access admin dashboard
2. **Manage Applications**: Approve/reject admissions
3. **Handle Contacts**: Reply to user messages
4. **View Statistics**: Monitor application stats

## 🔒 Security Features

- Session management with timeout
- CSRF protection
- Input validation
- SQL injection prevention
- Secure password handling

## 📧 Email Templates

The application includes pre-configured email templates in Urdu/Arabic for:
- Contact form confirmations
- Admission confirmations
- Application approvals/rejections
- Admin notifications

## 🌍 Internationalization

- **Primary**: Urdu (RTL)
- **Secondary**: Arabic
- **Technical**: English
- Custom fonts for proper Urdu/Arabic display

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 💡 Support

For support and questions:
- **Email**: [your-email]
- **Issues**: GitHub Issues tab
- **Documentation**: This README

## 🎯 Future Enhancements

- [ ] Student portal
- [ ] Online classes integration
- [ ] Payment gateway
- [ ] Mobile app
- [ ] Multi-language admin panel
- [ ] Advanced reporting

---

**Made with ❤️ for Islamic Education**
#   v i r t u a l - i s l a m i c - u n i v e r s i t y  
 