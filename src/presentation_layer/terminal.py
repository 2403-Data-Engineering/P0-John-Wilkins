'''
Key Concept (important for interviews)

This class is essentially your application controller:

It connects everything together
It sits between:
Presentation layer (menus)
Service layer (business logic)

Think of it like:

“Terminal is the brain coordinating UI and logic.”
'''

# Allows forward references in type hints (so classes can be referenced before they are fully defined)
from __future__ import annotations
from typing import TYPE_CHECKING

from service_layer.student_service import StudentService
from service_layer.professor_service import ProfessorService
from service_layer.class_service import ClassService
from service_layer.enrollment_service import EnrollmentService
from service_layer.report_service import ReportService

if TYPE_CHECKING:
    from presentation_layer.menu import Menu

# Import MainMenu here (avoid circular import by doing it at runtime)
from presentation_layer.menu import MainMenu

# Terminal acts as the main controller of the application
# It manages:
# - Application state (running or not)
# - Navigation between menus
# - Access to service layer
class Terminal:
    def __init__(self):
        self.running = True  # Fix: was `self.running: True` (annotation, not assignment)
        self.student_service = StudentService()
        self.professor_service = ProfessorService()
        self.class_service = ClassService()
        self.enrollment_service = EnrollmentService()
        self.report_service = ReportService(self.enrollment_service)
        self.current_menu = MainMenu(self)  # Fix: MainMenu is now imported above

    def navigate(self, menu: Menu):
        # Replaces the active menu; the run loop will display the new one
        self.current_menu = menu
    # Stops the application
    def quit(self):
        # Signals the run loop to stop on its next iteration
        self.running = False
        print("Quitting...")