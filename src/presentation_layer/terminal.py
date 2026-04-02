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
# TYPE_CHECKING prevents certain imports from running at runtime (avoids circular imports)
from typing import TYPE_CHECKING
# Import service layer classes (business logic layer)
from service_layer.student_service import StudentService
from service_layer.professor_service import ProfessorService
from service_layer.class_service import ClassService
from service_layer.enrollment_service import EnrollmentService
from service_layer.report_service import ReportService
# Only imported during type checking (not at runtime)
# Prevents circular dependency between Terminal and Menu
if TYPE_CHECKING:
    from presentation_layer.menu import Menu
# Import MainMenu at runtime (outside TYPE_CHECKING)
# This avoids circular import issues while still allowing usage
from presentation_layer.menu import MainMenu

# Terminal acts as the main controller of the application
# It manages:
# - Application state (running or not)
# - Navigation between menus
# - Access to service layer
class Terminal:
    def __init__(self):
        # Controls whether the application is running
        # Is your application running? If it is, you better go catch it.
        # (used in a loop elsewhere, likely in your main entry point)
        self.running = True  
        # Initialize all service layer objects
        # These handle business logic and data operations
        self.student_service = StudentService()
        self.professor_service = ProfessorService()
        self.class_service = ClassService()
        self.enrollment_service = EnrollmentService()
        self.report_service = ReportService()
        # Set the starting menu when the application launches
        self.current_menu = MainMenu(self)  
    # Changes the current menu (used for navigation between screens)
    def navigate(self, menu: Menu):
        self.current_menu = menu
    # Stops the application
    def quit(self):
        self.running = False
        print("Quitting...")