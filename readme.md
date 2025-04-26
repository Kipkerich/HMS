
# HealthSys - Basic Health Information System 🏥

A simple yet functional **Health Information System** built with **Django** (backend) and **Bootstrap** (frontend).  
It allows doctors (system users) to manage health programs, register clients, enroll clients in programs, and view client profiles through both the web app and an API.

---

## Features ✨
- **User Authentication**: Registration, Login, Logout.
- **Dashboard**: Displays total clients, programs, and enrollments.
- **Program Management**: Create and view health programs.
- **Client Registration**: Add new clients to the system.
- **Client Enrollment**: Enroll clients in one or multiple health programs.
- **Client Search**: Easily find clients by name.
- **Client Profile**: View full profile including enrolled programs.
- **API Access**: Expose client profiles via a JSON API.

---

## Tech Stack 🛠
- **Backend**: Django 5.2
- **Frontend**: Bootstrap 5
- **Database**: SQLite (default, easy setup)
- **Authentication**: Django built-in user system
- **API**: Django REST Framework (DRF)

---

## Setup Instructions 🚀

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/healthsys.git
   cd healthsys
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (admin account):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Visit the app at:**
   ```
   http://127.0.0.1:8000/
   ```

---

## API Endpoint 🌐
- **Client Profile API**  
  Retrieve client data (program enrollments) in JSON format:
  ```
  GET /api/client/<client_id>/
  ```

Example:
```bash
curl http://127.0.0.1:8000/api/client/1/
```

---

## Project Structure 📁
```
healthsystem/
├── core/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── dashboard.html
│   │   ├── create_program.html
│   │   ├── register_client.html
│   │   ├── enroll_client.html
│   │   └── client_profile.html
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── serializers.py
├── healthsystem/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── venv/   # (Not pushed to GitHub — added to .gitignore)
├── manage.py
├── requirements.txt
└── README.md
```

---




