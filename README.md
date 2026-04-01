# Kyle Plummer P0 Examples

I will put some example code for the P0 project here. 

I've added some basic examples for menus and terminal. Something to note is that I did this in the OOP way, where every entity I worked on was a class. It started to become apparent right away why this adds more difficulty than OOP-first languages. Type hints began to give me issues with circular imports, and I have too many references flying around already with only like 4 classes.

If I were to refactor this, I would start by making the Terminal a singleton, and not a class object. There will only ever need to be one terminal in the life of the program, the terminal we are presenting to the user. We never create a second one.

We start by loading in the main menu, which prompts the user for a menu selection. That input runs through a switch (called "match" in python) statement. Depending on the selection, different things happen. Most are not yet implemented, but the New Student menu and the Quit action are implemented. Selecting new student queues up the next menu and exits the function. Selecting quit sets the "running" variable to false, so next time we iterate the loop, we quit.