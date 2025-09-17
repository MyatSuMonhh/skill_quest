import os
import re
import string
import random
import time
import copy

# !!! THIS FILE CONTAINS FUNCTIONS AND DATA THAT ARE SHARED AMONG ALL FILES
# !!! LOGIC HERE HELPS TO OUTPUT DATA IN A GOOD LOOKING FORM, HELDS VALIDATION

# DEFINE CONSTANTS
# ---------------------------------------------------------------------------

# COLORS FOR GAME TEXT
COLORS = {
    "BLACK": "\033[30m",
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "RESET": "\033[0m",
}

# SIGNS TO INDICATE SPECIA LINES IN GAME MENU DRAWING
BORDER = "-"
SPACE = " "

# ---------------------------------------------------------------------------


# TEXT EDITING FUNCTIONS
# ---------------------------------------------------------------------------

# RETURN RAW TEXT OF THE STRING WITHOUNT FORMATING SIGNS
def strip_ansi_codes(text):
    return re.sub(r'\033\[\d+m', '', text)

# RETURN TEXT COLORED WITH GIVEN COLOR
def color_text(text, color):
    text = strip_ansi_codes(text)
    return color + text + COLORS["RESET"]

# RETURN TEXT CENTERED IN A GIVEN WIDTH
def center_text(text, window_width):
    stripped_text = strip_ansi_codes(text)
    padding_needed = (window_width - 2 - len(stripped_text)) // 2
    return ' ' * padding_needed + text + ' ' * (window_width - 2 - padding_needed - len(stripped_text))

# ADJUST LENGTH OF EACH ELEMENT OF ARRAY
# EACH ELEMENT HAS LENGTH OF THE LONGEST ELEMENT
def adjust_length(string_list):
    # FIND LENGTH OF THE LONGEST ELEMENT
    max_length = max(len(s) for s in string_list)
    
    # ADJUST LENGTH OF EACH ELEMENT BY ADDING EXTRA SPACES AT THE END
    padded_list = [s.ljust(max_length) for s in string_list]
    
    return padded_list

# RETURN STIRNG OF THE SAME LENGTH WITH RANDOM CHARACTERS
def randomize(input_string):
    # DEFINE CHARACTERS THAT CAN BE USED: ASCII CHARACTERS, DIGITS, PUNCTUATION MARKS AND SPACE
    all_characters = string.ascii_letters + string.digits + string.punctuation + ' '

    # GENERATE STRING OF RANDOM CHARACTERS WITH THE SAME LENGTH
    random_string = ''.join(random.choice(all_characters) for _ in range(len(input_string)))
    return random_string

# ---------------------------------------------------------------------------

# DATA INPUT VALIDATION
# ---------------------------------------------------------------------------

def validate(value, min_value, max_value):
    try:
        # Convert input to an integer
        value = int(value)
        # Check if the number is between 1 and 9
        if value < min_value or value > max_value:
            return(-1)
        else:
            return(1)
    except ValueError:
        # Handle the case where conversion to int fails
        return(0)

# ---------------------------------------------------------------------------

# RETURNS TRUE WITH THE GIVEN CHANCE
def random_event(chance):
    return random.random() < chance

# DATA DISPLAYING FUNCTIONS
# ---------------------------------------------------------------------------

# CLEAR CONSOLE SCREEN
def clear_console():
    # Clear the console based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

# DISPLAY EMPTY LINE
def empty_line(window_width):
    return "|" + " " * (window_width - 2) + "|"

# DISPLAY BORDER LINE
def border_line(window_width):
    return "+" + "-" * (window_width - 2) + "+"

# DISPLAY SCREEN 
# STRINGS IS A LIST OF STRINGS AND/OR LISTS THAT CONTAINS INFORMATION ABOUT THE SCREEN
def display(strings, window_width):
    clear_console()
    for line in strings:
        if(line == BORDER):
            print(border_line(window_width))
        elif(line == SPACE):
            print(empty_line(window_width))

        # FUNCTION CAN SERVE LIST, DISPLAYING EACH ELEMENT IN DIFFERENT LINES
        elif(type(line) is list):
            for i in line:
                #ADJUSTING LENGTH OF THE ELEMENT TO THE WIDTH OF THE SCREEN
                print("|" + (f"{i}").ljust(window_width - 2) + "|")
        else:
            print("|" + (f"{line}").ljust(window_width - 2) + "|")

# DISPLAY MENU OF THE GAME OR HOMEPAGE
def display_menu(game_data, chiper):

    # MAKE COPY OF GAME DATA SO. FUNCTION DOES NOT CHANGES ORIGINAL SOURCE
    data = copy.deepcopy(game_data)

    # FROMATING GAME DATA SO IT CAN BE PROPERLY DISPLAYED ACCORDING TO RULES

    # RANDOMIZE EACH MENU OPTIONS IF READING ABILITY IS NOT OPENED YET
    if chiper:
        data["game_title"] = color_text("AI UNABLE TO READ INSTRUCTIONS", COLORS["RED"])

        for i in range(len(data["menu_options"])):
            data["menu_options"][i] = center_text(randomize(data["menu_options"][i]), data["window_width"])

        data["main_menu_instruction"] = color_text("ENTER ANYTHING TO GO BACK, COMPLETE WORDLE TO TRAIN AI", COLORS["RED"])
    else:
        for i in range(len(data["menu_options"])):
            data["menu_options"][i] = center_text(data["menu_options"][i], data["window_width"])

    data["main_menu_instruction"] = center_text(data["main_menu_instruction"], data["window_width"])

    # OUTPUT DATA IS A SCREEN IN FORM OF STRINGS LIST
    output_data = []

    # ADD EXTRA DATA TO THE END OF SCREEN IN CASE OF ITS EXISTANC
    if "extra_information" in data:
        # Center data that is displayed after menu options in the center of the screen
        for i in range(len(data["extra_information"])):
            data["extra_information"][i] = center_text(data["extra_information"][i], data["window_width"])

        # Build the structure of the output screen
        output_data = [
            BORDER,
            center_text(color_text(f"{data["game_title"]}", COLORS["RED"]), data["window_width"]),
            BORDER,
            SPACE,
            data["menu_options"],
            SPACE,
            data["extra_information"],
            SPACE,
            data["main_menu_instruction"],
            BORDER,
        ]
    else:
        # Build the structure of the output screen without extradata
        output_data = [
            BORDER,
            center_text(color_text(f"{data["game_title"]}", COLORS["RED"]), data["window_width"]),
            BORDER,
            SPACE,
            data["menu_options"],
            SPACE,
            data["main_menu_instruction"],
            BORDER,
        ]
    
    display(output_data, data["window_width"])

# DISPLAY RULES OF THE GAME ACCORDING TO GAME DATA
def display_rules(game_data):
    data = game_data.copy()

    # Adjust the length of each instruction so that it is equal to the maximum element length
    data["instructions"][1] = adjust_length(data["instructions"][1])

    # Place instructions for users in the center of the screen
    for i in range(len(data["instructions"][1])):
        data["instructions"][1][i] = center_text(data["instructions"][1][i], data["window_width"])

    # Build the structure of rules screen
    output_data = [
        BORDER,
        center_text("\033[91mHOW TO PLAY\033[0m", data["window_width"]),
        BORDER,
        SPACE,
        center_text(data["instructions"][0], data["window_width"]),
        SPACE,
        data["instructions"][1],
        SPACE,
        center_text(color_text("TYPE ANYTHING TO GO TO HOMEPAGE", COLORS["RED"]), data["window_width"]),
        BORDER
    ]
    display(output_data, game_data["window_width"])



