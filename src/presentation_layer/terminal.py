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

import os
# Import MySQL connection (fix: was missing)
import mysql.connector
# Load environment variables from .env file (fix: was missing)
from dotenv import load_dotenv

from data_layer.student_dao import StudentDAO
from data_layer.professor_dao import ProfessorDAO
from data_layer.class_dao import ClassDAO
from data_layer.enrollment_dao import EnrollmentDAO

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
        load_dotenv()

        self.running = True

        self.connection = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DB"),
            port=int(os.getenv("PORT"))
        )


        
        self.student_dao = StudentDAO(self.connection)
        self.professor_dao = ProfessorDAO(self.connection)
        self.class_dao = ClassDAO(self.connection)
        self.enrollment_dao = EnrollmentDAO(self.connection)

        self.student_service = StudentService(self.student_dao)
        self.professor_service = ProfessorService(self.professor_dao)
        self.class_service = ClassService(self.class_dao)
        self.enrollment_service = EnrollmentService(self.enrollment_dao)
        self.current_menu = MainMenu(self)

    def navigate(self, menu: Menu):
        # Replaces the active menu; the run loop will display the new one
        self.current_menu = menu
    # Stops the application
    def quit(self):
        # Signals the run loop to stop on its next iteration
        self.running = False
        print("Quitting...")