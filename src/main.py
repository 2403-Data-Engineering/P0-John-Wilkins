from presentation_layer.terminal import Terminal
from service_layer.student_service import StudentService


if __name__ == "__main__":
    
    terminal = Terminal(StudentService())
    while(terminal.running):
        terminal.current_menu.render()
    print("...Goodbye!")