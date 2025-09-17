import time
import os
import random
import sys
import internal.utils as utils

# DEFINE GAME VARIABLES
# --------------------------------------------------------------------------------------------------------------------------------------------

# WIDTH OF THE GAME SCREEN
window_width = 70

# TITLE, DISPLAYED ON THE TOP OF THE SCREEN
game_title = utils.color_text("PINPOINT", utils.COLORS["RED"])

# OPTIONS THAT ARE DISPLAYED IN THE MENU
menu_options = ["1. EXIT", "2. START GAME", "3. RULES"]

# INSTRUCTIONS THAT ARE DISPAYED IN THE RULES PAGE
instructions = ["Identify the common category from given clues.", [" * Read Clue: Check the clue carefully.", " * Enter Guess: Type your category guess.", " * Next Clue: If wrong, get another clue."]]

# INSTRUCTION THAT IS PROVIDED FOR USER AT THE BOTTOM OF THE SCREEN
main_menu_instruction = "TYPE NUMBER TO GO TO THE FOLLOWIN PAGE"

# ASCII TITLE THAT IS DISPLAYED BEFOR GAME STARTS
askii_title = """
 .----------------.  .----------------.  .-----------------.
| .--------------. || .--------------. || .--------------. |
| |   ______     | || |     _____    | || | ____  _____  | |
| |  |_   __ \   | || |    |_   _|   | || ||_   \|_   _| | |
| |    | |__) |  | || |      | |     | || |  |   \ | |   | |
| |    |  ___/   | || |      | |     | || |  | |\ \| |   | |
| |   _| |_      | || |     _| |_    | || | _| |_\   |_  | |
| |  |_____|     | || |    |_____|   | || ||_____|\____| | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------' 
  .----------------.  .----------------.  .----------------.  .-----------------. .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |   ______     | || |     ____     | || |     _____    | || | ____  _____  | || |  _________   | |
| |  |_   __ \   | || |   .'    `.   | || |    |_   _|   | || ||_   \|_   _| | || | |  _   _  |  | |
| |    | |__) |  | || |  /  .--.  \  | || |      | |     | || |  |   \ | |   | || | |_/ | | \_|  | |
| |    |  ___/   | || |  | |    | |  | || |      | |     | || |  | |\ \| |   | || |     | |      | |
| |   _| |_      | || |  \  `--'  /  | || |     _| |_    | || | _| |_\   |_  | || |    _| |_     | |
| |  |_____|     | || |   `.____.'   | || |    |_____|   | || ||_____|\____| | || |   |_____|    | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

 """

# DIFFICULTY LEVELS OF THE GAMES, DIFFICULTY INCREASES WITH THE INCREASE OF THE INDEX OF ARRAY
# STRUCTURE: "WORD THAT USER SHOUL GUESS": [ARRAY OF CLUES THAT ARE PROVIDED TO USER]
data = [
    {
        "Apple": ["Fruit", "Red", "Pie", "Orchard", "Crunchy"],
        "Dog": ["Bark", "Pet", "Loyal", "Fetch", "Tail"],
        "House": ["Home", "Roof", "Walls", "Family", "Shelter"],
        "Book": ["Read", "Pages", "Story", "Library", "Knowledge"],
        "Tree": ["Leaves", "Branches", "Forest", "Nature", "Wood"]
    },
    {
        "Bicycle": ["Wheels", "Pedal", "Ride", "Handlebar", "Cycle"],
        "Computer": ["Screen", "Keyboard", "Internet", "Software", "Data"],
        "Mountain": ["Climb", "Peak", "Hike", "Nature", "Range"],
        "Chocolate": ["Sweet", "Candy", "Cocoa", "Dessert", "Treat"],
        "Ocean": ["Water", "Waves", "Salt", "Beach", "Marine"]
    },
    {
        "Algorithm": ["Code", "Process", "Data", "Solve", "Logic"],
        "Quantum": ["Physics", "Particle", "Theory", "Mechanics", "Energy"],
        "Renaissance": ["Art", "Culture", "Revival", "History", "Innovation"],
        "Hypothesis": ["Test", "Theory", "Experiment", "Science", "Research"],
        "Paradox": ["Contradiction", "Truth", "Statement", "Logic", "Dilemma"]
    }
]

# --------------------------------------------------------------------------------------------------------------------------------------------

# HELPER FUNCTIONS
# --------------------------------------------------------------------------------------------------------------------------------------------

# SERVES DISPLAYING OF STARTUP MENU OF THE GAME
def display_menu(game_data, chiper):
    utils.display_menu(game_data, chiper)

# SERVES DISPLAYING THE RULES PAGE OF THE GAME
def display_rules(game_data):
    utils.display_rules(game_data)

# SERVES DISPLAYING GAME SCREEN
def display_screen(game_data, clues, section):

    # Adjust game screen instruction to the center of the screen
    instruction = utils.center_text(utils.color_text("TYPE WORD TO GUESS IT, YOU HAVE 5 ATTEMPTS", utils.COLORS["RED"]), game_data["window_width"])

    # Adjust title to the center of the screen
    title = utils.center_text(utils.color_text(section, utils.COLORS["RED"]), game_data["window_width"]) 

    # Make shure to not change original data
    output_clues = clues.copy()

    # Center each clue on the screen
    for i in range(len(output_clues)):
        if output_clues[i] != "":
            output_clues[i] = utils.center_text(f"Clue {i+1}: " + output_clues[i], game_data["window_width"])
    
    # Build the structure of the displayed screen
    output_data = [
        utils.BORDER,
        title,
        utils.BORDER,
        utils.SPACE,
        output_clues,
        utils.SPACE,
        instruction,
        utils.BORDER
    ]
    
    utils.display(output_data, game_data["window_width"])

# DISPLAY RESULT OF THE GAME TO USER
def display_end_screen(game_data, won, word):

    # Center horizontaly word on the screen
    word = utils.center_text("WORD: " + utils.color_text(word, utils.COLORS["GREEN"]), game_data["window_width"])

    # Center title to the center of the screen and make it red
    title = utils.center_text(utils.color_text("PINPOINT", utils.COLORS["RED"]), game_data["window_width"])

    #  Center message to the center of the screen and make it red
    message = utils.center_text(utils.color_text("TRY ONE MORE TIME :>", utils.COLORS["RED"]), game_data["window_width"])

    #  Center instruction to the center of the screen and make it red
    instruction = utils.center_text(utils.color_text("TYPE ANYTHING TO GO HOME", utils.COLORS["RED"]), game_data["window_width"])

    # Display proper message if user won the game
    if(won):
        title = utils.center_text(utils.color_text("PINPOINT", utils.COLORS["GREEN"]), game_data["window_width"])
        message = utils.center_text(utils.color_text("CONGRATULATIONS!", utils.COLORS["GREEN"]), game_data["window_width"])

    # Build the structure of the displayed screen
    output_data = [
        utils.BORDER,
        title,
        utils.BORDER,
        utils.SPACE,
        word,
        utils.SPACE,
        message,
        utils.SPACE,
        instruction,
        utils.BORDER
    ]

    utils.display(output_data, game_data["window_width"])

# --------------------------------------------------------------------------------------------------------------------------------------------

# GAME LOGIC
# --------------------------------------------------------------------------------------------------------------------------------------------

def start_game(game_data):
    
    # Retrieve difficulty level from the game data
    level = game_data["difficulty"]

    # Randomly choose word that should be guessed from the following difficulty level
    word = random.choice(list(data[level]))

    # Retrieve the clues for the following word
    clues = data[level][word]

    # Adjust clues to the center of the screen
    clues = utils.adjust_length(clues)

    # Define number of current attempt
    attempts = 0

    # Defined clues that are currently displayed
    output_clues = []

    # Ask user to enter the guess
    while(True):

        display_screen(game_data, clues[:attempts+1] + [""] * (4 - attempts), game_data["game_title"])
        guess = input("Enter your guess: ")

        # Check if user guessed the word
        if guess.lower() == word.lower():
            print("You Won")
            display_end_screen(game_data, True, word)
            input("Enter command: ")
            return 1
        else:
            attempts +=  1
            # Check if user used or attempts
            if attempts >= 5:
                print("You lost the game")
                display_end_screen(game_data, False, word)
                input("Enter command: ")
                return -1

# SERVE STARTUP MENU OF THE GAME
def menu(game_data, chiper):
    utils.clear_console()

    # Display askii title for 2 seconds
    print(askii_title.center(window_width))
    time.sleep(1)

    # Message that is displayed if user provided incorrect input
    error_message = ""

    while True:

        display_menu(game_data, chiper)

        # Display error message if user provided incorrect data
        if(error_message != ""):
            print(error_message)

            # Reset message
            error_message = "" 

        # Request input from user
        command = input("Enter command: ")

        # Serve game exit
        if command == "1":
            return 0
        # Serve game start
        elif command == "2" and not chiper:
            return start_game(game_data)
        # Serve rules request
        elif command == "3" and not chiper:
            display_rules(game_data)
            input("Enter command: ")
        # Return user to main screen if game is not unlocked
        elif chiper:
            return 0
        # Ask user to input proper values
        else:
            error_message = utils.COLORS["RED"] + "Please, enter number from 1 to 3, representing your choice" + utils.COLORS["RESET"]


# --------------------------------------------------------------------------------------------------------------------------------------------

# STARTING POINT FOR THE GAME
def start(chiper, difficulty):
    # Retrieve game data and compose it to dictionary
    game_data = {
        "window_width": window_width,
        "game_title": utils.color_text(game_title, utils.COLORS["RED"]),
        "instructions": instructions,
        "menu_options": menu_options,
        "main_menu_instruction":  main_menu_instruction,
        "difficulty": difficulty
    }

    # Start main menu
    return menu(game_data, chiper)

