# Import the Terminal class (main application controller)
from presentation_layer.terminal import Terminal
from dotenv import load_dotenv
load_dotenv()

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

    '''
Big Picture

This file is your entry point (like main() in other languages):

Starts the app
Runs the loop
Hands control to the Terminal + Menus

If you want, next I can help you:

Add error handling to prevent crashes
Add a clean exit strategy (like saving state)
Or structure this like a production-ready CLI app
    '''