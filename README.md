# P0-John-Wilkins
🎓 College Administration System

A Python-based console application that models a college course registration system. The application manages professors, students, classes, and enrollments, supporting full CRUD operations, relational data integrity, and report generation in HTML and/or Markdown formats.

📌 Overview

This system simulates a real-world college administration environment with the following relationships:

Professor → Classes: One-to-Many
Student ↔ Classes: Many-to-Many (via enrollments)

The application follows a layered architecture and interacts with a MySQL relational database using parameterized SQL queries.

🏗️ Architecture

The project is structured into three main layers:

1. Presentation Layer
Console-based menu system
Handles all user input/output
Navigates between application features
2. Service Layer
Contains business logic
Enforces rules and constraints
Acts as a bridge between presentation and data layers
3. Data Layer
Handles all database interactions
Executes parameterized SQL queries
Performs CRUD operations and relationship queries
🧰 Technologies Used
Python 3
MySQL
mysql-connector-python (database connectivity)
Yattag (HTML report generation) (optional)
mdutils (Markdown report generation) (optional)
Stretch Technologies
SQLAlchemy (ORM alternative)
FastAPI (REST API layer)
🗄️ Database Design
Tables
professors
students
classes
enrollments (join table)
Key Features
Primary keys on all tables
Foreign key constraints for relationships
No cascade deletes (handled in application logic)
Optional soft deletes via is_active flag
Unique constraint on (student_id, class_id) to prevent duplicate enrollments
⚙️ Features
👨‍🏫 Professors
Add, view, update, and remove professors
Prevent deletion if assigned to classes
📚 Classes
Create classes with assigned professors
View and update class details
Delete classes
🎓 Students
Add, view, update, and remove students
Prevent deletion if enrolled in classes
🔗 Enrollment
Enroll students in classes
Drop students from classes
Prevent duplicate enrollments
📊 Reports
Student Enrollment Report
Lists all classes a student is enrolled in
Professor Summary Report
Lists all classes taught and enrolled students

Reports are generated as:

HTML (via Yattag)
Markdown (via mdutils)
🖥️ Console Interface
Menu-driven navigation system
Modular and reusable menu screens
Graceful handling of invalid input
Clear user prompts and feedback
🚀 Getting Started
Prerequisites
Python 3.x
MySQL Server
Installation
git clone https://github.com/yourusername/college-admin-system.git
cd college-admin-system
python -m venv venv
source venv/bin/activate  # (or venv\Scripts\activate on Windows)
pip install -r requirements.txt
Database Setup
Create a MySQL database:
CREATE DATABASE college_admin;
Run the provided schema script:
-- schema.sql
Update database connection settings in:
data/db_connection.py
▶️ Running the Application
python main.py
📁 Project Structure
college-admin-system/
│
├── presentation/     # Console menus (UI)
├── services/         # Business logic
├── data/             # Database access layer
├── reports/          # Report generation
├── models/           # Data models (optional)
├── schema.sql        # Database schema
├── main.py           # Entry point
└── README.md
🧪 Testing
Manual testing via console interface
Covers:
CRUD operations
Enrollment logic
Constraint enforcement
Report generation
📌 Design Decisions
Layered Architecture ensures separation of concerns
Parameterized SQL prevents SQL injection
No cascade deletes to enforce business logic at the application level
Soft deletes used to preserve historical data (optional)
🌟 Stretch Goals
Refactor data layer using SQLAlchemy ORM
Expose functionality via FastAPI REST API
Add automated testing (e.g., pytest)
Improve UI/UX (CLI enhancements)
📦 Deliverables
✔️ Source code in GitHub repository
✔️ ERD diagram included
✔️ Functional console application
✔️ Report generation (HTML/Markdown)
✔️ Ready for live demonstration
👤 Author

John Wilkins
Masters of Computer Science
University of Southern Mississippi