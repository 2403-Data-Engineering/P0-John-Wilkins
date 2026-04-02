# Import the Terminal class (main application controller)
from presentation_layer.terminal import Terminal


# This ensures the code only runs when this file is executed directly
# (and not when it's imported into another file)
if __name__ == "__main__":
    # Create an instance of the Terminal (starts the application)
    terminal = Terminal()
    # Main application loop
    # Keeps running until terminal.running is set to False
    while(terminal.running):
        # Render the current menu (handles user interaction)
        terminal.current_menu.render()
    # Runs after the loop ends (when user quits)
    print("...Goodbye!")