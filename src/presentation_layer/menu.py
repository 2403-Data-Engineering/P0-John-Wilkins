# Allows forward references in type hints
# so you can reference classes before thhey are fully defined
#Type checking doesn't work without these annotations from future
from __future__ import annotations
# Used to define abstract base classes (classes that are meant to be inherited from)
'''What is an abstract class and how do you define it in Python?

    An abstract class is a class that cannot be instantiated and often contains one or more abstract methods that must be implemented by subclasses.
    In Python, abstract classes are defined using the abc module and the ABC class.
    Abstract methods are defined with the @abstractmethod decorator.
'''
from abc import abstractmethod
# Used to avoid circular imports at runtime
from typing import TYPE_CHECKING
# We import our data models
from models.student import Student
from models.professor import Professor
from models.classes import Classes
# This block only runs during type checking (not at runtime)
# It prevents circular import issues with Terminal
if TYPE_CHECKING:
    from presentation_layer.terminal import Terminal
# Base Menu class acts as a template for all the other menus
class Menu:
    def __init__(self, terminal: Terminal):
        # Reference to the main terminal controller
        self.terminal: Terminal = terminal
# Abstract method forces all subclasses to implement render()
    @abstractmethod
    def render() -> None:
        pass

# Main menu users see first
class MainMenu(Menu):
    def render(self) -> None:
        # Displays the following menu options
        print("""
===========================
Welcome to uRevature Admin
1) Manage Students
2) Manage Professors
3) Manage Classes
4) Enrollment
5) Reports
Q) Quit
            """)
# Get user input and normalize it to lowercase
        user_input: str = input().lower()
        # Match user choice to the different actions
        match user_input:
            case "1":
                self.terminal.navigate(StudentMenu(self.terminal))
            case "2":
                self.terminal.navigate(ProfessorMenu(self.terminal))
            case "3":
                self.terminal.navigate(ClassMenu(self.terminal))
            case "4":
                self.terminal.navigate(EnrollmentMenu(self.terminal))
            case "5":
                self.terminal.navigate(ReportMenu(self.terminal))
            case "q":
                # Exit the application
                self.terminal.quit()
class StudentMenu(Menu):
    def render(self):
        print("""
Student Menu
1) Add Student
2) View All Students
3) Update Student
4) Delete Student
5) View Student Classes
6) Back
""")
        choice = input()

        match choice:
            case "1":
                self.terminal.navigate(NewStudentMenu(self.terminal))

            case "2":
                students = self.terminal.student_service.get_all()
                for s in students:
                    print(f"{s.student_id}: {s.first_name} {s.last_name}")

            case "3":
                student_id = int(input("Enter ID: "))
                student = self.terminal.student_service.get_by_id(student_id)
                if student:
                    student.first_name = input("New first name: ")
                    student.last_name = input("New last name: ")
                    self.terminal.student_service.update(student)

            case "4":
                student_id = int(input("Enter ID: "))
                self.terminal.student_service.delete(student_id)

            case "5":
                student_id = int(input("Enter ID: "))
                classes = self.terminal.enrollment_service.get_classes_by_student(student_id)
                for c in classes:
                    print(c.class_name)

            case "6":
                self.terminal.navigate(MainMenu(self.terminal))
class NewStudentMenu(Menu):
    def render(self):
        print("""
===========================
New Student Menu
""")
# Collect user input for the new student
        print("Please enter the following information for the new student.")
        # print("ID: ")
        # student_id: int = int(input())
        print("First name: ")
        first_name: str = input()
        print("Last name: ")
        last_name: str = input()
        print("Major: ")
        major: str = input()
        print("Email: ")
        email: str = input()
        print("Year: ")
        year: str = input()
# Create a new Student object based on their input
        new_student: Student = Student(None,first_name, last_name, major, email, year)
# Save student using service layer
        self.terminal.student_service.save(new_student)
# Return to main menu
        self.terminal.navigate(MainMenu(self.terminal))
class ProfessorMenu(Menu):
    def render(self):
        print("""
Professor Menu
1) Add Professor
2) View All Professors
3) Update Professor
4) Delete Professor
5) Back
""")
        choice = input()

        match choice:
            case "1":
                self.terminal.navigate(NewProfessorMenu(self.terminal))

            case "2":
                professors = self.terminal.professor_service.get_all()
                for p in professors:
                    print(f"{p.professor_id}: {p.first_name} {p.last_name}")

            case "3":
                pid = int(input("Enter ID: "))
                prof = self.terminal.professor_service.get_by_id(pid)
                if prof:
                    prof.first_name = input("New first name: ")
                    prof.last_name = input("New last name: ")
                    self.terminal.professor_service.update(prof)

            case "4":
                pid = int(input("Enter ID: "))
                self.terminal.professor_service.delete(pid)

            case "5":
                self.terminal.navigate(MainMenu(self.terminal))
# Menu for creating a new professor
class NewProfessorMenu(Menu):
    def render(self):
        print("""
===========================
New Professor Menu
""")
        print("Please enter the following information for the new professor.")
        # print("ID: ")
        # professor_id: int = int(input())
        print("First name: ")
        first_name: str = input()
        print("Last name: ")
        last_name: str = input()
        print("Department: ")
        department: str = input()
        print("Email: ")
        email: str = input()

        new_professor: Professor = Professor(None, first_name, last_name, department, email)
        self.terminal.professor_service.save(new_professor)

        self.terminal.navigate(MainMenu(self.terminal))
class ClassMenu(Menu):
    def render(self):
        print("""
Class Menu
1) Add Class
2) View All Classes
3) Update Class
4) Delete Class
5) View Students in Class
6) Back
""")
        choice = input()

        match choice:
            case "1":
                self.terminal.navigate(NewClassMenu(self.terminal))

            case "2":
                classes = self.terminal.class_service.get_all()
                for c in classes:
                    prof = self.terminal.professor_service.get_by_id(c.professor_id)
                    print(f"{c.class_id}:{c.class_name} - {prof.first_name} {prof.last_name}")

            case "3":
                cid = int(input("Enter Class ID: "))
                c = self.terminal.class_service.get_by_id(cid)
                if c:
                    c.class_name = input("New name: ")
                    c.professor_id = int(input("New professor ID: "))
                    self.terminal.class_service.update(c)

            case "4":
                cid = int(input("Enter Class ID: "))
                self.terminal.class_service.delete(cid)

            case "5":
                cid = int(input("Enter Class ID: "))
                students = self.terminal.enrollment_service.get_students_by_class(cid)
                for s in students:
                    print(f"{s.first_name} {s.last_name}")

            case "6":
                self.terminal.navigate(MainMenu(self.terminal))
class NewClassMenu(Menu):
    def render(self):
        print("""
===========================
New Class Menu
""")
        print("Please enter the following information for the new class.")
        # print("ID: ")
        # class_id: int = int(input())
        print("Class name: ")
        class_name: str = input()
        print("Professor ID: ")
        professor_id: int = int(input())

        new_class: Classes = Classes(None, class_name, professor_id)
        self.terminal.class_service.save(new_class)

        self.terminal.navigate(MainMenu(self.terminal))

# Menu for enrollment operations
class EnrollmentMenu(Menu):
    def render(self):
        print("""
===========================
Enrollment Menu
1) Enroll student in class
2) Drop student from class
3) Back to main menu
        """)
        # Get user choice
        choice: str = input().lower()
        # Do action based on their choice
        match choice:
            case "1":
                self.enroll_student()
            case "2":
                self.drop_student()
            case "3":
                self.terminal.navigate(MainMenu(self.terminal))
            case _:
                print("Invalid choice.")
                self.terminal.navigate(self)
# Handles enrolling a student into a class
    def enroll_student(self):
        print("Enter Student ID: ")
        student_id: int = int(input())
        # Retrieve student from service
        student = self.terminal.student_service.get_by_id(student_id)
        if not student:
            print("Student not found.")
            self.render()
            return

        print("Enter Class ID: ")
        class_id: int = int(input())
        # Retrieve class
        class_obj = self.terminal.class_service.get_by_id(class_id)
        if not class_obj:
            print("Class not found.")
            self.render()
            return
# Check if they are already enrolled in that class
        if self.terminal.enrollment_service.is_enrolled(student, class_obj):
            print(f"{student.first_name} {student.last_name} is already enrolled in {class_obj.class_name}.")
        else:
            # enroll them if not already enrolled
            self.terminal.enrollment_service.enroll(student, class_obj)
            print(f"{student.first_name} {student.last_name} has been enrolled in {class_obj.class_name}.")

        input("Press Enter to continue...")
        self.render()
# Handles removing a student from a class
    def drop_student(self):
        print("Enter Student ID: ")
        student_id: int = int(input())
        student = self.terminal.student_service.get_by_id(student_id)
        if not student:
            print("Student not found.")
            self.render()
            return

        print("Enter Class ID: ")
        class_id: int = int(input())
        classes = self.terminal.class_service.get_by_id(class_id)
        if not classes:
            print("Class not found.")
            self.render()
            return
# Check enrollment before dropping
        if self.terminal.enrollment_service.is_enrolled(student, classes):
            self.terminal.enrollment_service.drop(student, classes)
            print(f"{student.first_name} {student.last_name} has been removed from {classes.class_name}.")
        else:
            print(f"{student.first_name} {student.last_name} is not enrolled in {classes.class_name}.")

        input("Press Enter to continue...")
        self.render()

# Menu for generating reports
class ReportMenu(Menu):
    def render(self):
        print("""
===========================
Reports Menu
1) Student Enrollment Report
2) Professor Summary Report
3) Back to main menu
        """)
        choice: str = input().lower()
        match choice:
            case "1":
                self.student_enrollment_report()
            case "2":
                self.professor_summary_report()
            case "3":
                self.terminal.navigate(MainMenu(self.terminal))
            case _:
                print("Invalid choice.")
                self.render()
# Generates a report for a specific student
    def student_enrollment_report(self):
        print("Enter Student ID: ")
        student_id: int = int(input())
        student = self.terminal.student_service.get_by_id(student_id)
        if not student:
            print("Student not found.")
            self.render()
            return

        self.terminal.report_service.generate_student_report(student)
        print(f"Student enrollment report generated for {student.first_name} {student.last_name}.")
        input("Press Enter to continue...")
        self.render()

    def professor_summary_report(self):
        print("Enter Professor ID: ")
        professor_id: int = int(input())
        professor = self.terminal.professor_service.get_by_id(professor_id)
        if not professor:
            print("Professor not found.")
            self.render()
            return

        self.terminal.report_service.generate_professor_report(professor)
        print(f"Professor summary report generated for {professor.first_name} {professor.last_name}.")
        input("Press Enter to continue...")
        self.render()