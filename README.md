# Student Management System

A simple and user-friendly Student Management System built with Django.

## Features

- User Login and Logout
- Authentication protected pages
- Dashboard
- Add Student
- View Student Details
- Edit Student
- Delete Student
- Search students by name or student ID
- Student ID uniqueness validation
- Pagination
- Success and error messages
- Student creation date
- Myanmar timezone support
- Responsive and clean UI

## Technologies

- Python
- Django
- SQLite
- HTML
- CSS
- Django Templates
- Git & GitHub

## Project Structure

```text
Student_Management_System/
│
├── manage.py
├── db.sqlite3
├── README.md
│
├── student_management/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── students/
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    │
    ├── templates/
    │   └── students/
    │
    └── static/
        └── students/
            └── style.css