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
        self.terminal:Terminal = terminal

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
                print("TODO: IMPLEMENT ME")
            case "4":
                print("TODO: IMPLEMENT ME")
            case "5":
                print("TODO: IMPLEMENT ME")
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
                # Implement validation steps between prompts?

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
          
                # Implement validation steps between prompts?

                new_professor: Professor = Professor(first_name, last_name, department, email)
                self.terminal.professor_service.save(new_professor)

                self.terminal.navigate(MainMenu(self.terminal))