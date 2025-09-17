import os
import re
import sys
import random
import copy
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import internal.utils as utils

# DEFAUlT GAME DATA
# ------------------------------------------------------------

# Width of the screen
window_width = 70 

# Title of the game
game_title = "SUDOKU"

# Menu options
menu_options = ["1. EXIT", "2. START GAME", "3. RULES"]
main_menu_instruction = "TYPE NUMBER TO GO TO THE FOLLOWING PAGE"

# Instructions on the rules page
instructions = ["Fill the grid with numbers 1-9.", [" * Each row must have unique numbers.", " * Each column must have unique numbers.", " * Each 3x3 box must have unique numbers.", " * Start with given numbers to guide you.", " * Use logic, not guessing, to solve."]]

# Askii art, representing game title
askii_title = """
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |    _______   | || | _____  _____ | || |  ________    | || |     ____     | || |  ___  ____   | || | _____  _____ | |
| |   /  ___  |  | || ||_   _||_   _|| || | |_   ___ `.  | || |   .'    `.   | || | |_  ||_  _|  | || ||_   _||_   _|| |
| |  |  (__ \_|  | || |  | |    | |  | || |   | |   `. \ | || |  /  .--.  \  | || |   | |_/ /    | || |  | |    | |  | |
| |   '.___`-.   | || |  | '    ' |  | || |   | |    | | | || |  | |    | |  | || |   |  __'.    | || |  | '    ' |  | |
| |  |`\____) |  | || |   \ `--' /   | || |  _| |___.' / | || |  \  `--'  /  | || |  _| |  \ \_  | || |   \ `--' /   | |
| |  |_______.'  | || |    `.__.'    | || | |________.'  | || |   `.____.'   | || | |____||____| | || |    `.__.'    | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
 
 """

# ------------------------------------------------------------

difficulties = [
    # EASY DIFFICULTY BOARDS 4x4, NORMAL 6x6, HARD 9x9
    {
        "boards": [
            [
                [1, 0, 0, 0],
                [2, 0, 1, 0],
                [4, 0, 0, 1],
                [0, 1, 4, 2]
            ],
            [
                [3, 1, 4, 0],
                [0, 0, 1, 0],
                [1, 2, 3, 4],
                [0, 3, 0, 1]
            ],
        ],
        "board_width": 4,
        "board_height": 4,
        "group_width": 2,
        "group_height": 2,
        "lives": 3,
    },
    {
        "boards": [
            [
                [5, 1, 6, 0, 0, 4],
                [3, 4, 0, 5, 0, 1],
                [0, 0, 0, 2, 0, 6],
                [6, 2, 5, 1, 0, 3],
                [4, 5, 1, 0, 0, 2],
                [0, 6, 0, 0, 0, 5],
            ],
            [
                [0, 6, 0, 0, 5, 0],
                [0, 0, 3, 0, 6, 0],
                [1, 0, 5, 0, 0, 2],
                [0, 0, 2, 1, 3, 0],
                [3, 1, 0, 0, 0, 4],
                [2, 0, 4, 3, 0, 6]
            ],
        ],
        "board_width": 6,
        "board_height": 6,
        "group_width": 3,
        "group_height": 2,
        "lives": 3,
    },
    {
        "boards": [
            [
                [0, 0, 0, 0, 0, 1, 0, 3, 5],
                [0, 2, 3, 0, 9, 0, 0, 0, 6],
                [0, 1, 6, 0, 3, 0, 0, 9, 0],
                [0, 0, 5, 6, 8, 3, 0, 0, 7],
                [3, 0, 0, 0, 0, 2, 6, 5, 0],
                [0, 6, 7, 0, 0, 0, 4, 8, 0],
                [6, 0, 2, 8, 0, 7, 3, 1, 0],
                [4, 0, 0, 0, 0, 0, 0, 7, 8],
                [7, 0, 0, 1, 0, 0, 2, 6, 4],
            ],
            [
                [0, 6, 0, 8, 1, 5, 0, 2, 0],
                [0, 0, 0, 0, 3, 0, 8, 0, 0],
                [0, 5, 0, 7, 2, 0, 6, 9, 1],
                [0, 0, 0, 0, 0, 2, 0, 3, 0],
                [5, 4, 0, 0, 0, 0, 0, 6, 2],
                [3, 0, 8, 1, 5, 6, 9, 0, 0],
                [0, 0, 0, 4, 8, 0, 0, 5, 0],
                [0, 9, 0, 0, 6, 0, 0, 8, 3],
                [0, 0, 5, 2, 9, 3, 0, 1, 6],
            ],
            [
                [0, 0, 0, 6, 0, 1, 4, 8, 2],
                [0, 0, 8, 0, 0, 2, 0, 0, 0],
                [3, 6, 0, 0, 8, 7, 5, 0, 0],
                [0, 0, 9, 0, 7, 6, 1, 0, 8],
                [2, 1, 0, 8, 0, 4, 6, 7, 0],
                [0, 0, 6, 3, 0, 5, 0, 0, 0],
                [0, 0, 0, 0, 6, 0, 0, 0, 0],
                [0, 2, 5, 0, 4, 0, 3, 0, 1],
                [9, 7, 1, 0, 2, 3, 0, 4, 0],
            ],
        ],
        "board_width": 9,
        "board_height": 9,
        "group_width": 3,
        "group_height": 3,
        "lives": 2,
    }
]

# PRINT THE SUDOKU BOARD ACCORDING TO THE DIFFICULTY
def print_board(board, width, height, group_width, group_height):
    os.system('cls||clear')

    # Find number of groups in the board horizontally and vertically
    group_x_number = width // group_width
    group_y_number = height // group_height

    # Print top line that will represent column number
    x_hint_line = ""
    for i in range(group_x_number):
        x_hint_line += "   " + " ".join(map(lambda x: str(x), list(range(i * group_width + 1, i * group_width + 1 + group_width))))
    print(x_hint_line)

    # Print border
    print(" + " + "-" * (width * 2 + (group_x_number - 1) * 3 - group_x_number))

    for row in range(height):
        # Print border if row between 2 groups
        if row % group_height == 0 and row != 0:
            print("   " + "-" * (width * 2 + (group_x_number - 1) * 3 - group_x_number))
        # Print hint that will represent row number
        print(row+1, end="| ")
        # Print numbers of sudoku
        for col in range(width):
            # Print border if it is between number groups
            if col % group_width == 0 and col != 0:
                print("|", end=" ")
                # Print number or space
            print(board[row][col] if board[row][col] != 0 else ".", end=" ")
        print()

# CHECK IF THE NUMBER COULD BE PLACED OR NOT
def is_valid(board, group_width, group_height, row, col, num):
    # Check if there is this number in column
    for x in range(len(board[row])):
        if board[row][x] == num:
            return False
    # Check if number is in a row
    for y in range(len(board)):
        if board[y][col] == num:
            return False
    # Check if number is in number group
    start_row = row - row % group_height
    start_col = col - col % group_width
    for i in range(group_height):
        for j in range(group_width):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

# Check if some number can be placed in the border
def check_board_validity(board, group_width, group_height):
    # Going through each element
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 0:
                # Try to put each number in empty place
                if not can_place_any_number(board, group_width, group_height, row, column):
                    return (False, row, column)
    return True, -1, -1

# IF THERE IS NO EMPTY LOCATION,THE PLAYER WINS
def find_empty_location(board):
    # Go through each location and check is it is empty
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == 0:
                return (row, column)
    return None

# CHECK IF ANY NUMBER CAN BE PLACED IN THE GIVEN CELL
def can_place_any_number(board, group_width, group_height, row, column):
    # Try every number for the given cell
    for num in range(1, len(board) + 1):
        if is_valid(board, group_width, group_height, row, column, num):
            return True
    return False

#STARTING PAGE
def main(game_data):
    # Choose random board from given difficulties
    # Make shure to not change original data
    board = copy.deepcopy(difficulties[game_data["difficulty"]]["boards"][random.randint(0, 1)])

    # Retrieve how many times user can make mistake
    lives = game_data["lives"]

    # Print board of sudoku
    print_board(board, game_data["board_width"], game_data["board_height"], game_data["group_width"], game_data["group_height"])
    print(f"You have {lives} lives")
    
    while True:
        row = 0
        column = 0

        while True:
            # Ask user to choose row
            row = input(f"Enter row (1-{game_data['board_height']}): ")
            # Continue to ask user to enter row until it is valid
            row_valid = utils.validate(row, 1, game_data['board_height'])
            while(row_valid != 1):
                # Print error message
                if(row_valid == -1):
                    print(f"{utils.COLORS['RED']}Row should be number between 1 and {game_data['board_height']}{utils.COLORS['RESET']}")
                elif(row_valid == 0):
                    print(f"{utils.COLORS['RED']}Please, enter number between 1 and {game_data['board_height']} representing row{utils.COLORS['RESET']}")
                row = input(f"Enter row (1-{game_data['board_height']}): ")
                row_valid = utils.validate(row, 1, game_data['board_height'])
            row = int(row)
            row -= 1

            # Ask user to choose column
            column = input(f"Enter column (1-{game_data['board_width']}): ")
            # Continue to ask user to enter column until it is valid
            column_valid = utils.validate(column, 1, game_data['board_width'])
            while(column_valid  != 1):
                # Print error message
                if(column_valid  == -1):
                    print(f"{utils.COLORS['RED']}Column should be number between 1 and {game_data['board_width']}{utils.COLORS['RESET']}")
                elif(column_valid  == 0):
                    print(f"{utils.COLORS['RED']}Please, enter number between 1 and {game_data['board_width']} representing column{utils.COLORS['RESET']}")
                column = input(f"Enter column (1-{game_data['board_width']}): ")
                column_valid = utils.validate(column, 1, game_data['board_width'])
            column = int(column)
            column -= 1

            # If user chosed empty space, go further
            if(board[row][column] == 0):
                break
            # Ask to input choose empty space
            else:
                print("Chose empty place")

                find_empty_location

        # Ask to choose number
        num = input(f"Enter number (1-{game_data['board_width']}): ")
        # Continue to ask user to enter number until it is valid
        num_valid = utils.validate(num, 1, game_data['board_width'])
        while(num_valid != 1):
            if(num_valid == -1):
                print(f"{utils.COLORS['RED']}Number should be number between 1 and {game_data['board_width']}{utils.COLORS['RESET']}")
            elif(num_valid == 0):
                print(f"{utils.COLORS['RED']}Please, enter number between 1 and {game_data['board_width']} representing number that you want to pass{utils.COLORS['RESET']}")
                num = input(f"Enter number (1-{game_data['board_width']}): ")
            num = input(f"Enter number (1-{game_data['board_width']}): ")
            num_valid = utils.validate(num, 1, game_data['board_width'])
        num = int(num)
        
        # Check if number can be placed in the given cell
        if is_valid(board, game_data["group_width"], game_data["group_height"], row, column, num):
            # Place number in the cell
            board[row][column] = num

            # Check board validity
            board_valid, row, column = check_board_validity(board, game_data["group_width"], game_data["group_height"])
            # If no number cannot be placed in some cell of the game, user loses the game
            if not board_valid:
                # Print proper message
                print_board(board, game_data["board_width"], game_data["board_height"], game_data["group_width"], game_data["group_height"])
                print(f"No number can be placed for place: ({row+1}, {column+1})")
                print("You lost, try one more time")
                print("Type Enter to return to homepage")
                input()
                return -1
  
            # If there are no empty spaces, user won the game
            if not find_empty_location(board):
                # Print proper message
                print_board(board, game_data["board_width"], game_data["board_height"], game_data["group_width"], game_data["group_height"])
                print("Congratulations! You've solved the Sudoku.")
                print("Enter anything to go to homepage")
                input()
                return 1
            print_board(board, game_data["board_width"], game_data["board_height"], game_data["group_width"], game_data["group_height"])
        else:
            #PLAYER LOSE LIFE IF THE MOVE IS INVALID
            print("\033[31mInvalid move.\033[0m")
            lives -= 1
            print(f"Lives left: {lives}")
            if(lives == 0):
                print("Lives ended, you lost, try one more time")
                input()
                return -1

def run_game(chiper, game_data):
    utils.clear_console()

    # Print askii title before game starts
    print(askii_title.center(window_width))
    time.sleep(1)

    # Error message the will be displayed if user provides incorrect input
    error_message = ""

    running = True
    while running:
        utils.display_menu(game_data, chiper)

        # Display error message if user provided incorrect data
        if(error_message != ""):
            print(error_message)

            # Reset message
            error_message = "" 
        
        # Ask to input command
        command = input("Enter command: ")

        # Serve exiting
        if(command == "1" or chiper):
            return 0
        # Serve game startup
        elif(command == "2"):
            return main(game_data)
        # Serve request for rules
        elif(command == "3"):
            utils.display_rules(game_data)
            input("Enter command: ")
        # Serve incorrect input
        else:
            error_message = utils.COLORS["RED"] + "Please, enter number from 1 to 3, representing your choice" + utils.COLORS["RESET"]


def start(chiper, difficulty, game_data = {}):
    # Compose default game data into game_data
    if(game_data == {}):
        game_data = {
            "window_width": window_width,
            "game_title": utils.color_text(game_title, utils.COLORS["RED"]),
            "instructions": instructions,
            "menu_options": menu_options,
            "main_menu_instruction":  main_menu_instruction,
            "difficulty": difficulty,
            "board_width": difficulties[difficulty]["board_width"],
            "board_height": difficulties[difficulty]["board_height"],
            "group_height": difficulties[difficulty]["group_height"],
            "group_width": difficulties[difficulty]["group_width"],
            "lives": difficulties[difficulty]["lives"]
        }
    
    return run_game(chiper, game_data)



