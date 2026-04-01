
from __future__ import annotations
from typing import TYPE_CHECKING

from service_layer.student_service import StudentService


if TYPE_CHECKING:
    from presentation_layer.menu import Menu


class Terminal:
    def __init__(self, student_service: StudentService):
        from presentation_layer.menu import MainMenu
        self.current_menu = MainMenu(self)
        self.running = True
        self.student_service = student_service


    def navigate(self, menu: Menu):
        
        self.current_menu = menu

    def quit(self):
        self.running = False
        print("Quitting...")
