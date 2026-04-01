
from __future__ import annotations
from typing import TYPE_CHECKING

from service_layer.student_service import StudentService
from service_layer.professor_service import ProfessorService
from service_layer.class_service import ClassService
from service_layer.enrollment_service import EnrollmentService
from service_layer.report_service import ReportService


if TYPE_CHECKING:
    from presentation_layer.menu import Menu


class Terminal:
    def __init__(self):
        self.running: True
        self.student_service = StudentService()
        self.professor_service = ProfessorService()
        self.class_service = ClassService()
        self.enrollment_service = EnrollmentService()
        self.report_service = ReportService()
        self.current_menu = MainMenu(self)


    def navigate(self, menu: Menu):
        
        self.current_menu = menu

    def quit(self):
        self.running = False
        print("Quitting...")
