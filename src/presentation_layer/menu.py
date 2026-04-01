from __future__ import annotations
from abc import abstractmethod
from typing import TYPE_CHECKING

from models.student import Student
from models.professor import Professor
from models.classes import Classes

if TYPE_CHECKING:
    from presentation_layer.terminal import Terminal

class Menu:
    def __init__(self, terminal: Terminal):
        self.terminal: Terminal = terminal

    @abstractmethod
    def render() -> None:
        pass


class MainMenu(Menu):
    def render(self) -> None:
        print("""
===========================
Welcome to uRevature Admin
1) Create new student
2) Create new professor
3) Create new class
4) Enroll student in class
5) Run report
Q) Quit
        """)

        user_input: str = input().lower()
        match user_input:
            case "1":
                self.terminal.navigate(NewStudentMenu(self.terminal))
            case "2":
                self.terminal.navigate(NewProfessorMenu(self.terminal))
            case "3":
                self.terminal.navigate(NewClassMenu(self.terminal))
            case "4":
                self.terminal.navigate(EnrollmentMenu(self.terminal))
            case "5":
                self.terminal.navigate(ReportMenu(self.terminal))
            case "q":
                self.terminal.quit()

class NewStudentMenu(Menu):
    def render(self):
        print("""
===========================
New Student Menu
""")
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

        new_student: Student = Student(first_name, last_name, major, email, year)
        self.terminal.student_service.save(new_student)

        self.terminal.navigate(MainMenu(self.terminal))

class NewProfessorMenu(Menu):
    def render(self):
        print("""
===========================
New Professor Menu
""")
        print("First name: ")
        first_name: str = input()
        print("Last name: ")
        last_name: str = input()
        print("Department: ")
        department: str = input()
        print("Email: ")
        email: str = input()

        new_professor: Professor = Professor(first_name, last_name, department, email)
        self.terminal.professor_service.save(new_professor)

        self.terminal.navigate(MainMenu(self.terminal))

class NewClassMenu(Menu):
    def render(self):
        print("""
===========================
New Class Menu
""")
        print("Class name: ")
        class_name: str = input()

        new_class: Classes = Classes(class_name)
        self.terminal.class_service.save(new_class)

        self.terminal.navigate(MainMenu(self.terminal))

class EnrollmentMenu(Menu):
    def render(self):
        print("""
===========================
Enrollment Menu
1) Enroll student in class
2) Drop student from class
3) Back to main menu
        """)
        choice: str = input().lower()
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

    # Fix: enroll_student and drop_student were outdented outside the class
    def enroll_student(self):
        print("Enter Student ID: ")
        student_id: str = input()
        student = self.terminal.student_service.get_by_id(student_id)
        if not student:
            print("Student not found.")
            self.render()
            return

        print("Enter Class ID: ")
        class_id: str = input()
        class_obj = self.terminal.class_service.get_by_id(class_id)
        if not class_obj:
            print("Class not found.")
            self.render()
            return

        if self.terminal.enrollment_service.is_enrolled(student, class_obj):
            print(f"{student.first_name} {student.last_name} is already enrolled in {class_obj.name}.")
        else:
            self.terminal.enrollment_service.enroll(student, class_obj)
            print(f"{student.first_name} {student.last_name} has been enrolled in {class_obj.name}.")

        input("Press Enter to continue...")
        self.render()

    def drop_student(self):
        print("Enter Student ID: ")
        student_id: str = input()
        student = self.terminal.student_service.get_by_id(student_id)
        if not student:
            print("Student not found.")
            self.render()
            return

        print("Enter Class ID: ")
        class_id: str = input()
        class_obj = self.terminal.class_service.get_by_id(class_id)
        if not class_obj:
            print("Class not found.")
            self.render()
            return

        if self.terminal.enrollment_service.is_enrolled(student, class_obj):
            self.terminal.enrollment_service.drop(student, class_obj)
            print(f"{student.first_name} {student.last_name} has been removed from {class_obj.name}.")
        else:
            print(f"{student.first_name} {student.last_name} is not enrolled in {class_obj.name}.")

        input("Press Enter to continue...")
        self.render()

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

    def student_enrollment_report(self):
        print("Enter Student ID: ")
        student_id: str = input()
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
        professor_id: str = input()
        professor = self.terminal.professor_service.get_by_id(professor_id)
        if not professor:
            print("Professor not found.")
            self.render()
            return

        self.terminal.report_service.generate_professor_report(professor)
        print(f"Professor summary report generated for {professor.first_name} {professor.last_name}.")
        input("Press Enter to continue...")
        self.render()