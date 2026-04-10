# 📚 College Course Registration System (P0 Project)

## 📖 Overview

This project is a **terminal-based Student Management System** built using Python. It allows users to manage students, professors, classes, and enrollments through a structured, layered architecture.

The application demonstrates core software engineering concepts including:

* Data Access Objects (DAO)
* Service Layer abstraction
* Relational database design
* CRUD operations
* Object-Oriented Programming (OOP)

---

## 🚀 Features

* 👨‍🎓 Manage Students (Create, Read, Update, Delete)
* 👩‍🏫 Manage Professors
* 🏫 Manage Classes
* 📝 Handle Student Enrollments
* 🔗 Relational database integration
* 🧱 Layered architecture (Presentation → Service → DAO → Database)

---

## 🏗️ Architecture

This project follows a **multi-layered architecture**:

```
Presentation Layer (Terminal UI)
        ↓
Service Layer (Business Logic)
        ↓
DAO Layer (Database Access)
        ↓
Database (SQL)
```

### 🔹 Layers Explained

* **Presentation Layer**: Handles user input/output via terminal
* **Service Layer**: Contains business logic and validation
* **DAO Layer**: Handles database queries and data persistence
* **Database**: Stores relational data (students, professors, classes, enrollments)

---

## 🗄️ Database Schema

### Tables:

* **Student**

  * student_id (PK)
  * first_name
  * last_name
  * email

* **Professor**

  * professor_id (PK)
  * first_name
  * last_name
  * department
  * email

* **Class**

  * class_id (PK)
  * class_name
  * professor_id (FK)

* **Enrollment**

  * enrollment_id (PK)
  * student_id (FK)
  * class_id (FK)

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/2403-Data-Engineering/P0-John-Wilkins.git
cd P0-John-Wilkins
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

* Ensure your SQL database is running
* Create the required tables (see schema above)
* Update database connection settings in your config file

---

## ▶️ Running the Application

```bash
python main.py
```

---

## 🧪 Example Usage

* Add a new student
* Assign a professor to a class
* Enroll a student in a class
* View all enrollments

---

## 🛠️ Technologies Used

* Python
* SQL (MySQL / PostgreSQL / SQLite)
* OOP Principles
* DAO Design Pattern

---

## 📂 Project Structure

```
src/
│── presentation_layer/
│   └── terminal.py
│
│── service_layer/
│   └── services.py
│
│── dao/
│   └── *.py
│
│── models/
│   └── *.py
│
│── main.py
```

---

## 🧠 Key Concepts Demonstrated

* Separation of Concerns
* Dependency Injection
* Data Modeling & Relationships
* Error Handling
* Clean Code Practices

---

## 🐞 Known Issues

* Input validation could be improved
* Limited UI (terminal-only)
* No authentication system

---

## 👤 Author

**John Wilkins**

* Graduate Student – Computer Science
* University of Southern Mississippi

---

## 📜 License

This project is for educational purposes.


[1]: https://www.sciencedirect.com/science/article/abs/pii/S0950584922000775?utm_source=chatgpt.com "How ReadMe files are structured in open source Java projects - ScienceDirect"
