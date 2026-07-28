# Student Management System

A web-based **Student Management System** built with **Django** that allows users to securely manage student records and provides a dedicated Host/Admin dashboard for monitoring registered users and overall system statistics.

## Features

### User Authentication

* User registration and login
* Logout functionality
* Password reset functionality
* User profile
* Role-based access for normal users and Host/Admin

### Student Management

* Add new students
* View student details
* Edit student information
* Delete student records
* Upload student profile images
* Student ID card
* Search students
* Filter students by course
* Sort student records

### Host/Admin Dashboard

* Dedicated Host/Admin dashboard
* View registered normal users
* Search registered users
* Pagination for registered users
* View total registered users
* View total students
* View total courses
* View average student age

### Data Export

* Export student records to Excel
* Host/Admin can export registered user data to Excel

## Technologies Used

* Python
* Django
* SQLite
* HTML5
* CSS3
* Bootstrap 5
* Bootstrap Icons
* JavaScript
* OpenPyXL

## Project Structure

```text
Student_Management_System/
│
├── accounts/
│   ├── migrations/
│   ├── templates/
│   │   └── accounts/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── students/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   └── students/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── student_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AnujKumar0109/Student-Management-System.git
```

### 2. Open the Project Directory

```bash
cd Student-Management-System
```

### 3. Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Windows PowerShell:

```bash
venv\Scripts\Activate.ps1
```

Windows CMD:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create a Superuser

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal to create the Host/Admin account.

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

```text
http://127.0.0.1:8000/
```

## User Roles

### Normal User

A normal registered user can:

* Log in to the system
* Add students
* View their own students
* Edit student records
* Delete student records
* Search and filter students
* Export their student records to Excel
* View student details
* Generate student ID cards

### Host/Admin

The Host/Admin can:

* Access the Host Dashboard
* View registered normal users
* Search registered users
* View system statistics
* Export registered users to Excel

## Excel Export

The system provides Excel export functionality using **OpenPyXL**.

Normal users can export their own student records.

Host/Admin users can export registered normal user information.

## Security

The application uses Django authentication and login protection to restrict access to authenticated users.

The Host Dashboard is restricted to users with staff privileges.

Users can only manage their own student records.

## Future Improvements

* Deploy the application online
* Add PostgreSQL database support
* Add student ID card PDF generation
* Add email notifications
* Add advanced Host/Admin user management
* Add charts and analytics
* Add REST API
* Improve automated testing
* Add cloud media storage

## Author

**Anuj Kumar**

GitHub:
https://github.com/AnujKumar0109

## License

This project is created for educational and portfolio purposes.
