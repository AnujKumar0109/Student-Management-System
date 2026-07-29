# 🎓 Student Management System

<p align="center">
  <strong>A modern, secure, and responsive Django-based web application for managing student records, users, and administrative operations.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-5.2-darkgreen?logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap&logoColor=white" alt="Bootstrap">
  <img src="https://img.shields.io/badge/Database-SQLite-blue?logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Excel-Export-green?logo=microsoftexcel&logoColor=white" alt="Excel">
  <img src="https://img.shields.io/badge/Status-Active-success" alt="Status">
</p>

<p align="center">
  <a href="https://student-management-system-k96h.onrender.com">
    <img src="https://img.shields.io/badge/Live-Demo-success?style=for-the-badge&logo=render&logoColor=white" alt="Live Demo">
  </a>
  <a href="https://github.com/AnujKumar0109/Student-Management-System">
    <img src="https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github&logoColor=white" alt="GitHub Repository">
  </a>
</p>

---

# 🚀 Live Demo

<p align="center">
  🌐 <strong>Live Application</strong>
</p>

<p align="center">
  <a href="https://student-management-system-k96h.onrender.com" target="_blank">
    <strong>👉 View Live Application</strong>
  </a>
</p>



---

# 📌 About The Project

**Student Management System** is a full-stack web application developed using **Python and Django** to simplify and organize student record management.

The application provides a secure and user-friendly platform where authenticated users can manage their student records, while authorized Host/Admin users can monitor registered users and view overall system statistics.

The system includes:

* 🔐 User authentication and authorization
* 👤 User profile management
* 🛡️ Role-based access control
* 🎓 Complete student CRUD operations
* 🔍 Search and filtering
* ↕️ Student record sorting
* 📄 Pagination
* 📊 Dashboard statistics
* 📥 Excel data export
* 🪪 Student ID card generation
* 🖼️ Student image upload
* 🛡️ Dedicated Host/Admin dashboard

---

# ✨ Key Features

## 🔐 Authentication & User Management

* 📝 User registration
* 🔑 Secure login and logout
* 🔄 Password reset functionality
* 👤 User profile management
* 🛡️ Role-based access control
* 🔒 Protected pages using Django authentication
* 🚫 Unauthorized access protection

---

## 🎓 Student Management

Authenticated users can manage their student records with:

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

## 🛡️ Host/Admin Dashboard

Authorized Host/Admin users have access to a dedicated administrative dashboard.

Features include:

* 👥 View registered users
* 🔎 Search users by username or email
* 📊 View total registered users
* 🎓 View total students
* 📚 View total courses
* 📈 View average student age
* 📄 Paginated user records
* 📥 Export registered user information to Excel

---

# 📊 Dashboard Statistics

| Statistic         | Description                      |
| ----------------- | -------------------------------- |
| 👥 Total Users    | Total number of registered users |
| 🎓 Total Students | Total number of student records  |
| 📚 Total Courses  | Number of unique courses         |
| 📈 Average Age    | Average age of students          |

---

# 📊 Data Export

The application provides Excel export functionality using **OpenPyXL**.

## 👨‍🎓 Normal Users

Users can export their student records containing:

* Roll Number
* Student Name
* Email
* Phone
* Course
* Age
* Address
* Date of Birth

## 🛡️ Host/Admin

Authorized administrators can export registered user information containing:

* Username
* Email
* Date Joined
* Last Login

---

# 🖥️ Application Workflow

## 👤 Normal User Workflow

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
Generate Student ID Card
   ↓
Export Data to Excel
```

## 🛡️ Host/Admin Workflow

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

# 🧰 Technologies Used

| Technology                | Purpose                          |
| ------------------------- | -------------------------------- |
| 🐍 Python 3.11            | Backend programming              |
| 🌐 Django 5.2             | Web framework                    |
| 🗄️ SQLite                | Database                         |
| 🎨 HTML5                  | Page structure                   |
| 🎨 CSS3                   | Custom styling                   |
| 🅱️ Bootstrap 5.3         | Responsive UI                    |
| ⚡ JavaScript              | Client-side functionality        |
| 📊 OpenPyXL               | Excel file generation            |
| 🛡️ Django Authentication | Authentication and authorization |
| 📄 ReportLab              | PDF/ID card generation           |

---

# 🏗️ Project Structure

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
├── media/
├── static/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/AnujKumar0109/Student-Management-System.git
```

## 2️⃣ Navigate to the Project Directory

```bash
cd Student-Management-System
```

## 3️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

## 4️⃣ Activate the Virtual Environment

### Windows CMD

```bash
venv\Scripts\activate
```

### Windows PowerShell

```bash
venv\Scripts\Activate.ps1
```

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 6️⃣ Apply Database Migrations

```bash
python manage.py migrate
```

## 7️⃣ Create a Superuser

```bash
python manage.py createsuperuser
```

## 8️⃣ Run the Development Server

```bash
python manage.py runserver
```

## 9️⃣ Open the Application

Visit:

```text
http://127.0.0.1:8000/
```

---

# 👥 User Roles & Permissions

## 👨‍🎓 Normal User

Normal authenticated users can:

* 🔐 Login securely
* 👤 Manage their profile
* ➕ Add students
* 👁️ View students
* ✏️ Edit student records
* 🗑️ Delete student records
* 🔍 Search students
* 📚 Filter students by course
* ↕️ Sort student records
* 🪪 Generate student ID cards
* 📥 Export student data to Excel

## 🛡️ Host/Admin

Authorized Host/Admin users can:

* 📊 Access the Host/Admin dashboard
* 👥 View registered users
* 🔎 Search users
* 📈 View system statistics
* 📥 Export user data to Excel
* 🔒 Access restricted administrative functionality

---

# 🔒 Security

The application includes several security features:

* 🔐 Login-required views
* 🛡️ Protected administrative dashboard
* 👤 User-specific student records
* 🚫 Unauthorized access protection
* 🔑 Django authentication system
* 🔒 CSRF protection
* 🗃️ Sensitive files protected using `.gitignore`

> ⚠️ **Production Security:** Never expose your Django `SECRET_KEY`, database credentials, API keys, or other sensitive configuration values. Store them securely using environment variables.

---

# 🚀 Deployment

The **Student Management System** is deployed and hosted on **Render**.

## 🌐 Live Application

👉 **Live URL:**
https://student-management-system-k96h.onrender.com

<p align="center">
  <a href="https://student-management-system-k96h.onrender.com">
    <img src="https://img.shields.io/badge/🚀_Open_Live_Application-success?style=for-the-badge" alt="Open Live Application">
  </a>
</p>

For production deployment, make sure to configure:

* `SECRET_KEY`
* `DEBUG=False`
* `ALLOWED_HOSTS`
* Database configuration
* Static file handling
* Media file storage
* Environment variables

---

# 📸 Screenshots

Add screenshots of your application inside a `screenshots/` directory.

## 🔐 Login Page

![Login Screenshot](screenshots/login.png)

## 🏠 Dashboard

![Dashboard Screenshot](screenshots/dashboard.png)

## 🎓 Student Management

![Students Screenshot](screenshots/students.png)

## 🪪 Student ID Card

![ID Card Screenshot](screenshots/idcard.png)

## 🛡️ Host/Admin Dashboard

![Host Dashboard Screenshot](screenshots/host-dashboard.png)

---

# 🔮 Future Enhancements

Possible future improvements include:

* 📧 Email notifications
* 📱 Fully optimized mobile experience
* 📊 Advanced analytics and charts
* 📄 PDF student report generation
* 🔔 Real-time notifications
* ☁️ Cloud-based media storage
* 🗄️ PostgreSQL production database
* 🔍 Advanced student filtering
* 📅 Attendance management
* 💰 Fee management
* 📚 Course and subject management

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature branch
3. Make your changes
4. Commit your changes
5. Push the branch
6. Open a Pull Request

---

# 👨‍💻 Author

## Anuj Kumar

<p>
  <a href="https://github.com/AnujKumar0109">
    <img src="https://img.shields.io/badge/GitHub-AnujKumar0109-black?logo=github" alt="GitHub">
  </a>
</p>

* **GitHub Profile:** https://github.com/AnujKumar0109
* **Project Repository:** https://github.com/AnujKumar0109/Student-Management-System
* **Live Application:** https://student-management-system-k96h.onrender.com

---

# 📄 License

This project is developed for **educational, learning, and portfolio purposes**.

---

<p align="center">
  ⭐ <strong>If you like this project, don't forget to give it a star!</strong> ⭐
</p>

<p align="center">
  <strong>Built with ❤️ using Python, Django & Bootstrap</strong>
</p>
