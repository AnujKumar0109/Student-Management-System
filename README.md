# 🎓 Student Management System

<p align="center">
  <strong>A modern Django-based web application for managing student records, users, and administrative operations.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-5.2-darkgreen?logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap&logoColor=white" alt="Bootstrap">
  <img src="https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Excel-Export-green?logo=microsoftexcel&logoColor=white" alt="Excel">
  <img src="https://img.shields.io/badge/Status-Active-success" alt="Status">
</p>

---

## 📌 About The Project

**Student Management System** is a full-stack web application developed using **Python and Django** to simplify student record management.

The application provides a secure and user-friendly interface where registered users can manage their own student records, while **Host/Admin users** can monitor registered users and view overall system statistics.

The system includes authentication, role-based access control, student CRUD operations, search and filtering, Excel data export, student ID cards, and a dedicated administrative dashboard.

---

## ✨ Key Features

### 🔐 Authentication & User Management

* 📝 User registration
* 🔑 Secure login and logout
* 🔄 Password reset functionality
* 👤 User profile
* 🛡️ Role-based access control
* 🔒 Protected pages using Django authentication

---

### 🎓 Student Management

* ➕ Add new students
* 👁️ View detailed student information
* ✏️ Edit student records
* 🗑️ Delete student records
* 🖼️ Upload student profile images
* 🪪 Generate student ID cards
* 🔍 Search student records
* 📚 Filter students by course
* ↕️ Sort student records
* 📄 Paginate large student lists

---

### 🛡️ Host/Admin Dashboard

Host/Admin users have access to a dedicated dashboard with:

* 👥 View all registered normal users
* 🔎 Search users by username or email
* 📊 View total registered users
* 🎓 View total students
* 📚 View total courses
* 📈 View average student age
* 📄 Paginated user records
* 📥 Export registered users to Excel

---

### 📊 Data Export

The application supports Excel export using **OpenPyXL**.

👨‍🎓 **Normal Users**

* Export their own student records

🛡️ **Host/Admin**

* Export registered user information

---

## 🖥️ Application Overview

### 👤 Normal User Workflow

```text
Register
   ↓
Login
   ↓
Dashboard
   ↓
Add Student
   ↓
Manage Student Records
   ↓
Search / Filter / Sort
   ↓
View Student Details
   ↓
Generate ID Card
   ↓
Export Data to Excel
```

### 🛡️ Host/Admin Workflow

```text
Host/Admin Login
       ↓
Host Dashboard
       ↓
View Registered Users
       ↓
Search Users
       ↓
View System Statistics
       ↓
Export User Data to Excel
```

---

## 🧰 Technologies Used

| Technology                    | Purpose                                |
| ----------------------------- | -------------------------------------- |
| 🐍 **Python**                 | Backend programming                    |
| 🌐 **Django**                 | Web application framework              |
| 🗄️ **SQLite**                | Database                               |
| 🎨 **HTML5**                  | Page structure                         |
| 🎨 **CSS3**                   | Styling                                |
| 🅱️ **Bootstrap 5**           | Responsive UI                          |
| ⚡ **JavaScript**              | Client-side functionality              |
| 📊 **OpenPyXL**               | Excel file generation                  |
| 🛡️ **Django Authentication** | User authentication and access control |

---

## 🏗️ Project Structure

```text
Student_Management_System/
│
├── 📁 accounts/
│   ├── 📁 migrations/
│   ├── 📁 templates/
│   │   └── 📁 accounts/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── 📁 students/
│   ├── 📁 migrations/
│   ├── 📁 templates/
│   │   ├── base.html
│   │   └── 📁 students/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── 📁 student_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── 📄 manage.py
├── 📄 requirements.txt
├── 📄 .gitignore
└── 📄 README.md
```

---

## ⚙️ Installation & Setup

Follow the steps below to run the project locally.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AnujKumar0109/Student-Management-System.git
```

### 2️⃣ Navigate to the Project

```bash
cd Student-Management-System
```

### 3️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 4️⃣ Activate the Virtual Environment

**Windows PowerShell**

```bash
venv\Scripts\Activate.ps1
```

**Windows CMD**

```bash
venv\Scripts\activate
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 6️⃣ Apply Database Migrations

```bash
python manage.py migrate
```

### 7️⃣ Create a Superuser

```bash
python manage.py createsuperuser
```

Enter your username, email, and password when prompted.

### 8️⃣ Start the Development Server

```bash
python manage.py runserver
```

### 9️⃣ Open the Application

Visit:

```text
http://127.0.0.1:8000/
```

---

## 👥 User Roles & Permissions

### 👨‍🎓 Normal User

Normal users can:

* 🔐 Login securely
* 👤 Manage their profile
* ➕ Add students
* 👁️ View their students
* ✏️ Edit their student records
* 🗑️ Delete their student records
* 🔍 Search students
* 📚 Filter students by course
* ↕️ Sort student records
* 🪪 View student ID cards
* 📥 Export their student data to Excel

### 🛡️ Host/Admin

Host/Admin users can:

* 🔐 Access the Host Dashboard
* 👥 View registered users
* 🔎 Search registered users
* 📊 View overall system statistics
* 📥 Export registered users to Excel
* 🚫 Access is restricted from normal student management operations

---

## 📊 Dashboard Statistics

The Host Dashboard provides an overview of the system, including:

| Statistic         | Description                         |
| ----------------- | ----------------------------------- |
| 👥 Total Users    | Total registered normal users       |
| 🎓 Total Students | Total students stored in the system |
| 📚 Total Courses  | Number of unique courses            |
| 📈 Average Age    | Average age of all students         |

---

## 📥 Excel Export

The system provides separate Excel export functionality based on user role.

### 👨‍🎓 Normal User

Exports:

* Roll Number
* Email
* Phone
* Course
* Age
* Address
* Date of Birth

### 🛡️ Host/Admin

Exports:

* Username
* Email
* Date Joined
* Last Login

---

## 🔒 Security

The project uses Django's built-in security and authentication features.

Security features include:

* 🔐 Login-required protected views
* 🛡️ Staff-based Host/Admin access
* 👤 User-specific student data access
* 🚫 Unauthorized access prevention
* 🔑 Django authentication system
* 🔒 CSRF protection
* 🗃️ Sensitive files excluded using `.gitignore`

> ⚠️ For production deployment, configure environment variables for sensitive settings such as `SECRET_KEY` and database credentials.

---

## 🚀 Future Improvements

The following features can be added in future versions:

* ☁️ Deploy the application online
* 🐘 PostgreSQL database support
* 📄 Complete student ID card PDF generation
* 📧 Email notifications
* 👥 Advanced Host/Admin user management
* 📊 Interactive charts and analytics
* 🔌 REST API integration
* 🧪 Expanded automated testing
* ☁️ Cloud media storage
* 📱 Progressive Web App support
* 🌙 Dark mode
* 🔔 Notification system

---

## 📸 Screenshots

Add screenshots of your application here to showcase the project.

### 🔐 Login Page

> Add your login screenshot here.

### 🎓 Student Dashboard

> Add your student dashboard screenshot here.

### 👥 Student Management

> Add your student list screenshot here.

### 🛡️ Host Dashboard

> Add your Host Dashboard screenshot here.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

To contribute:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push the branch
6. Create a Pull Request

---

## 👨‍💻 Author

### Anuj Kumar

🐙 GitHub:
https://github.com/AnujKumar0109

💼 Project Repository:
https://github.com/AnujKumar0109/Student-Management-System

---

## 📄 License

This project is developed for **educational, learning, and portfolio purposes**.

---

<p align="center">
  ⭐ If you find this project useful, consider giving it a star!
</p>

<p align="center">
  <strong>Built with ❤️ using Python & Django</strong>
</p>
