# Allows use of 'Menu' as a type hint string before the class is fully defined
from __future__ import annotations
# TYPE_CHECKING is False at runtime — used to guard imports that are only
# needed for type hints, preventing circular import errors
from typing import TYPE_CHECKING
# Import all service classes that Terminal will instantiate and own
from service_layer.student_service import StudentService
from service_layer.professor_service import ProfessorService
from service_layer.class_service import ClassService
from service_layer.enrollment_service import EnrollmentService
from service_layer.report_service import ReportService
# Only import Menu during type checking (not at runtime), breaking the
# circular dependency: Terminal -> MainMenu -> Menu -> Terminal
if TYPE_CHECKING:
    from presentation_layer.menu import Menu

# Import MainMenu here (avoid circular import by doing it at runtime)
# Runtime import of MainMenu — safe here because TYPE_CHECKING is False,
# so the guard above never ran this path
from presentation_layer.menu import MainMenu


class Terminal:
    def __init__(self):
        # Loop flag; set to False to exit the app
        self.running = True  
        # Instantiate one shared copy of each service — all menus will
        # reference these via the Terminal instance passed to them
        self.student_service = StudentService()
        self.professor_service = ProfessorService()
        self.class_service = ClassService()
        self.enrollment_service = EnrollmentService()
        self.report_service = ReportService()
        # Start on the main menu; pass self so menus can call navigate/quit
        self.current_menu = MainMenu(self)  

    def navigate(self, menu: Menu):
        # Replaces the active menu; the run loop will display the new one
        self.current_menu = menu

    def quit(self):
        # Signals the run loop to stop on its next iteration
        self.running = False
        print("Quitting...")