# Bookmark Saver

## 📌 Project Overview
Bookmark Saver is a Django-based web application that allows users to save, manage, and organize their bookmarks efficiently using a clean web interface.

This project was built as part of a hackathon submission.

---

## 🚀 Features
- User authentication (login & logout)
- Save bookmarks with title and URL
- View and manage saved bookmarks
- Simple and clean UI using Django templates
- Admin panel for management

---

## 🧰 Tech Stack
- Backend: Django
- Frontend: HTML, CSS, Django Templates
- Database: SQLite
- Deployment: Render

---

## ⚙️ Installation & Setup (Local)
1. Clone the repository  
   ```bash
   git clone <repo-url>
   cd bookmarkSaver
Create virtual environment


python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
Install dependencies


pip install -r requirements.txt
Run migrations


python manage.py migrate
Run server


python manage.py runserver

##🌐 Live Demo
Deployed on Render:
👉 [https://your-project-name.onrender.com](https://bookmarksaver-djangotemplate.onrender.com/)

🧑‍💻 Usage
Register or login as a user

Add bookmark details

View bookmarks on dashboard

Admin users can manage data via /admin

🔐 Admin Access
To access admin panel:


/admin
Create superuser:


python manage.py createsuperuser
📁 Project Structure (Simplified)
arduino

bookmarkSaver/
├── home/
├── authentication/
├── templates/
├── static/
├── db.sqlite3
├── manage.py

🏁 Hackathon Notes
Focused on simplicity and usability

Designed to solve a real-world bookmarking problem

Built within limited time constraints
