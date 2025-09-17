import random
import tkinter
import time
import os
import re
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import internal.utils as utils

# DEFINE DEFAULT SETTINGS FOR THE GAME
# ----------------------------------------------------------------------

# VARIABLE THAT STORES THE WIDTH OF THE SCREEN OF THE GAME
window_width = 70 

# MENU PAGE DATA
menu_options = ["1. EXIT", "2. START GAME", "3. RULES"]
main_menu_instruction = "TYPE NUMBER TO GO TO THE FOLLOWING PAGE"

# RULES PAGE DATA
game_title = "MEMORY GAME"
instructions = ["Memorize the location of emojis in 3 tries.", [" * 9 emojis will be displayed in 3 seconds.", " * Everything will disappear after 3 seconds", " * One emoji from the table will pop up.", " * You should type its location"]]

askii_title = """
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  _________   | || | ____    ____ | || |     ____     | || |     _____    | || |     _____    | |
| | |_   ___  |  | || ||_   \  /   _|| || |   .'    `.   | || |    |_   _|   | || |    |_   _|   | |
| |   | |_  \_|  | || |  |   \/   |  | || |  /  .--.  \  | || |      | |     | || |      | |     | |
| |   |  _|  _   | || |  | |\  /| |  | || |  | |    | |  | || |   _  | |     | || |      | |     | |
| |  _| |___/ |  | || | _| |_\/_| |_ | || |  \  `--'  /  | || |  | |_' |     | || |     _| |_    | |
| | |_________|  | || ||_____||_____|| || |   `.____.'   | || |  `.___.'     | || |    |_____|   | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
 
 """

# DIFFICULTY LEVELS OF THE GAME, DIFFICULTY INCREASE WITH THE INCREASE OF INDEX
difficulties = [
    {"width": 3, "height": 3, "attempts": 3, "show_time": 5},
    {"width": 4, "height": 3, "attempts": 3, "show_time": 6},
    {"width": 5, "height": 3, "attempts": 3, "show_time": 7}
]

# ----------------------------------------------------------------------

# HELPER FUNCTIONS
# ----------------------------------------------------------------------

# GENERATE RANDOM EMOJIES
def generate_random_emoji():
    # Unicode range for emoji is roughly from U+1F600 to U+1F64F
    random_code_point = random.randint(0x1F600, 0x1F64F)
    return chr(random_code_point)

# RETURNS IF EMOJI IS IN THE TABLE
def is_in_table(table, emoji):
    for row in table:
        for element in row:
            if emoji == element:
                return True
    return False

# GENERATE TABLE OF EMOJIS WITH GIVEN WIDTH AND HEIGHT, ALL EMOJIS IN THE TABLE ARE UNIQUE
def generate_emoji_table(width, height):
    table = []
    for i in range(height):
        table.append([])
        for j in range(width):
            emoji = generate_random_emoji()
            while(is_in_table(table, emoji)): # make shure that generated emoji is not in the table
                emoji = generate_random_emoji()
            table[i].append(emoji)
    return table

# DISPLAYING EMOJI TABLE, FOR EACH EMOJI IT'S NUMBER IS DISPLAYED
def display_emoji_table(table):
    print()
    for i in range(len(table)):
        print(" ", end = "")
        for j in range(len(table[i])):
            print(f"{(i*len(table[i])+j+1):02d}{table[i][j]} ", end = "")
        print()
    print()

# ----------------------------------------------------------------------

# MAIN LOGIC OF EMOJI GAME
# ----------------------------------------------------------------------

# RUN GAME WITH GIVEN GAME SETTINGS WHEN USER CHOSES "2. START GAME"
def start_game(game_data):

    # EXTRACTING GAME DATA 
    width = game_data["width"]
    height = game_data["height"]
    attempts = game_data["attempts"]
    show_time = game_data["show_time"]

    # GENERATING TABLE WITH RANDOM EMOJIES
    emoji_table = generate_emoji_table(width, height)

    # CHOSING RANDOM EMOJI FROM TABLE, SAVING IT'S POSITION
    emoji_y = random.randint(0, height - 1)
    emoji_x = random.randint(0, width - 1)

    # CALCULATING NUMBER OF CHOSEN EMOJI THAT USER NEEDS TO RECOVER
    emoji_num = emoji_y * width + emoji_x + 1


    # DISPLAYING EMOJI TABLE IN THE TERMINAL
    display_emoji_table(emoji_table)
    
    # WAIT FOR SHOW_TIME SECONDS SO GAMER CAN MEMORIZE EMOJI POSITIONS
    time.sleep(show_time)

    # EMOJIS DISSAPEAR
    utils.clear_console()

    current_attempt = 0

    # ASK TO INPUT NUMBER OF EMOJI
    print(f"Emoji: {emoji_table[emoji_y][emoji_x]}")
    
    # START TO GET THE CORRECT ANSWER IN GIVEN TRIALS
    while current_attempt < attempts:
        answer = input(f'Enter numbers from 1 to {width * height} that corresponds to the following emoji: ')
        
        # ENSURE THAT USER INPUT IS A NUMBER BETWEEN POSSIBLE VALUES
        validation = utils.validate(answer, 1, width * height)
        if validation == 1:
            answer = int(answer)
            if answer == emoji_num:
                # GAMER WON THE GAME
                print('Well Done!')
                return 1
            else:
                # ANSWER IS INCORRECT
                # DECREASE NUMBER OF POSSIBLE ATTEMPTS
                print('Wrong!')
                current_attempt += 1
                print(f'{attempts - current_attempt} trails left')
                continue
        # DISPLAY PROPER MESSAGE SO USER CAN UNDERSTAND ERROR IN HIS OR HER INPUT
        elif validation == -1:
            print("Please, input number between 1 and 9")
        else:
            print("Only numbers are allowed")

    # END GAME IF USER USED ALL HIS OR HER ATTEMPTS
    print("You have used all your attempts.")
    return -1

# SERVING MENU OF THE GAME
def menu(chiper, game_data): 

    utils.clear_console()

    print(askii_title.center(window_width))
    time.sleep(1)

     # Error message the will be displayed if user provides incorrect input
    error_message = ""

    while True:
        utils.display_menu(game_data, chiper) # display menu of the game, chiper it in case if readinf ability is not opened

        # Display error message if user provided incorrect data
        if(error_message != ""):
            print(error_message)

            # Reset message
            error_message = "" 
        
        # Ask user for command
        choice = input("Enter command: ") 

        if choice == "1" or chiper:
            # exit the game
            print("Exiting the game...")
            return 0
        elif choice == "2":
            utils.clear_console()
            game_result = start_game(game_data) # run the game and recieve result
            if game_result == 1:
                # serve winning option
                print("You won! Press any key to return to exit.") 
                input()
                os.system('clear')
                return 1
            elif game_result == -1:
                #serve losing option
                print("You lost. Press any key to return to exit.")
                input()
                os.system('clear')
                return -1
        elif choice == "3":
            # display rules
            utils.display_rules(game_data)
            input("Enter command: ")
        else:
            # Serve incorrect input
            error_message = utils.COLORS["RED"] + "Please, enter number from 1 to 3, representing your choice" + utils.COLORS["RESET"]

# CALL FUNCTION TO RUN THE GAME FROM HOMEPAGE
def start(chiper, difficulty, game_data={}):
    if game_data == {}:
        game_data = {
            "window_width":             window_width,
            "game_title":               utils.color_text(game_title, utils.COLORS["RED"]),
            "instructions":             instructions,
            "menu_options":             menu_options,
            "main_menu_instruction":    main_menu_instruction,
            "width":                    difficulties[difficulty]["width"],
            "height":                   difficulties[difficulty]["height"],
            "attempts":                 difficulties[difficulty]["attempts"],
            "show_time":                difficulties[difficulty]["show_time"],
        }
    return menu(chiper, game_data)


