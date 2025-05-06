# EduStream - User Management System

This repository contains two architectural implementations of a user management system for EduStream:

- 🧱 `app.py` → **Monolithic Architecture**
- 🔗 `user_service.py` & `device_service.py` → **Microservices Architecture**

---

## 🧱 Monolithic Architecture

### 📄 File: `app.py`

A single Flask application handling both user registration and device login (with a 2-device limit per user) using a shared SQLite database.

### ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install flask flask_sqlalchemy
2. Run the monolith app:

bash
Copy
Edit
python app.py
Endpoints:

POST /register
Payload:

json
Copy
Edit
{ "email": "user@example.com" }
POST /login
Payload:

json
Copy
Edit
{ "email": "user@example.com", "device_id": "device123" }



## 🔗 Microservices Architecture
### 📁 Files:
user_service.py → Manages user registration

device_service.py → Manages device login and enforces 2-device limit

Each service has its own SQLite database (users_micro.db and devices_micro.db respectively).

▶️ How to Run
Install dependencies:

bash
Copy
Edit
pip install flask flask_sqlalchemy
Run both services in separate terminals:

User Service:

bash
Copy
Edit
python user_service.py
Device Service:

bash
Copy
Edit
python device_service.py
Endpoints:

POST http://localhost:5001/register
Payload:

json
Copy
Edit
{ "email": "user@example.com" }
POST http://localhost:5002/login
Payload:

json
Copy
Edit
{ "email": "user@example.com", "device_id": "device123" }
