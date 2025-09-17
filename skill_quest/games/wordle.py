import random
import os
import time
import re
import internal.utils as utils

correct_word = ""
max_attempts = 6
window_width = 50  # Set the width of the game window

# List of possible 5-letter words (Generated using ChatGPT)
difficulties = [
    # Easy level 
    {'WORDS': ["APPLE", "BEACH", "CLOUD", "DANCE", "EARTH", "FRUIT", "GRASS", "HOUSE", "MAGIC", "OCEAN", "PLANT", "QUIET", "RIVER", "SUGAR", "TABLE", "UNDER", "VOICE", "WATER", "YIELD", "ZEBRA"]},
    # Medium level 
    {'WORDS': ["BRAID", "CRUST", "DRIFT", "EMBER", "FROST", "GLOOM", "HOARD", "IVORY", "KNEEL", "LAPSE", "MIRTH", "NICHE", "PRONE", "QUEST", "RINSE", "STINT", "TWEAK", "VIGOR", "WAVER", "ZEAL"]},
    # Hard level 
    {'WORDS': ["AZURE", "BROIL", "CHAFF", "DOUSE", "ECLAT", "FJORD", "GRIPE", "HOIST", "KNAVE", "LITHE", "MYRRH", "NADIR", "QUELL", "REBUS", "SMIRK", "THRUM", "UMBER", "VEXED", "WIGHT", "YAWED"]}
]

# Define color codes for feedback (used ChatGPT to find color codes)
GREEN = "\033[42m"  
YELLOW = "\033[43m"
GRAY = "\033[100m"
RESET = "\033[0m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to remove ANSI color codes for accurate centering
def strip_ansi_codes(text):
    return re.sub(r'\033\[\d+m', '', text)

# Centering the text within borders
def center_text(text):
    stripped_text = strip_ansi_codes(text)
    padding_needed = (window_width - 2 - len(stripped_text)) // 2
    return ' ' * padding_needed + text + ' ' * (window_width - 2 - padding_needed - len(stripped_text))

splash = """ 
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | _____  _____ | || |     ____     | || |  _______     | || |  ________    | || |   _____      | || |  _________   | |
| ||_   _||_   _|| || |   .'    `.   | || | |_   __ \    | || | |_   ___ `.  | || |  |_   _|     | || | |_   ___  |  | |
| |  | | /\ | |  | || |  /  .--.  \  | || |   | |__) |   | || |   | |   `. \ | || |    | |       | || |   | |_  \_|  | |
| |  | |/  \| |  | || |  | |    | |  | || |   |  __ /    | || |   | |    | | | || |    | |   _   | || |   |  _|  _   | |
| |  |   /\   |  | || |  \  `--'  /  | || |  _| |  \ \_  | || |  _| |___.' / | || |   _| |__/ |  | || |  _| |___/ |  | |
| |  |__/  \__|  | || |   `.____.'   | || | |____| |___| | || | |________.'  | || |  |________|  | || | |_________|  | |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
 
 """

# Display ASCII art splash screen
def display_splash_screen():
    clear_screen()
    print(splash.center(window_width))
    time.sleep(1)
    clear_screen()


# Display main menu
def display_menu():
    print("+" + "-" * (window_width - 2) + "+")
    print("|" + center_text("\033[91mWORDLE GAME\033[0m") + "|")
    print("+" + "-" * (window_width - 2) + "+")
    print("|" + " " * (window_width - 2) + "|")
    print("|" + center_text("1. EXIT") + "|")
    print("|" + center_text("2. START GAME") + "|")
    print("|" + center_text("3. RULES") + "|")
    print("|" + " " * (window_width - 2) + "|")
    print("|" + center_text("TYPE NUMBER TO GO TO THE FOLLOWING PAGE") + "|")
    print("+" + "-" * (window_width - 2) + "+")

# Display game rules
def display_rules():
    clear_screen()
    print("+" + "-" * (window_width - 2) + "+")
    print("|" + center_text("HOW TO PLAY") + "|")
    print("+" + "-" * (window_width - 2) + "+")
    print("|" + " " * (window_width - 2) + "|")
    print("|" + center_text("Guess the Wordle in 6 tries.") + "|")
    print("|" + " " * (window_width - 2) + "|")
    print("|" + "  * Each guess must be a valid 5-letter word.".ljust(window_width - 2) + "|")
    print("|" + "  * The color of the tiles will change to show".ljust(window_width - 2) + "|")
    print("|" + "    how close your guess was to the word.".ljust(window_width - 2) + "|")
    print("|" + " " * (window_width - 2) + "|")
    print("|" + center_text("EXAMPLES") + "|")
    print("|" + " " * (window_width - 2) + "|")

    # Wordle examples in ASCII art style
    example_line_1 = f"|   {GREEN} W {RESET}   O   R   D   Y{' ' * 26}|"
    example_line_2 = f"|   L   {YELLOW} I {RESET}   G   H   T{' ' * 26}|"
    example_line_3 = f"|   R   O   G   {GRAY} U {RESET}   E{' ' * 26}|"
    
    # Aligning each example line and explanation within the box
    print(example_line_1)
    print("|   W is in the word and in the correct spot.    |")
    print("|" + " " * (window_width - 2) + "|")

    print(example_line_2)
    print("|   I is in the word but in the wrong spot.      |")
    print("|" + " " * (window_width - 2) + "|")

    print(example_line_3)
    print("|   U is not in the word in any spot.            |")
    print("|" + " " * (window_width - 2) + "|")
    
    print("|" + center_text("Press any key to return to the main menu.") + "|")
    print("+" + "-" * (window_width - 2) + "+")
    input("Enter command: ")

def display_wordle_grid(history, window_width=50, show_letters=True, show_only_attempts=False):
    # ANSI color codes for colored backgrounds (used ChatGPT to find color codes)
    green_bg = "\033[42m"  
    yellow_bg = "\033[43m" 
    gray_bg = "\033[100m"  
    reset = "\033[0m"


    empty_cell = "⬛"       # Empty cell for unused attempts

    # Define the appearance and width of each cell
    cell_width = 2 
    space_between_cells = "  "
    row_content_width = (cell_width + len(space_between_cells)) * 5 + 2
    padding = (window_width - row_content_width) // 2

    # Display the centered grid with borders
    print(" " * (padding - 2) + "+" + "-" * (row_content_width + 2) + "+")  # Top border
    for row in range(6):  # 6 attempts
        if show_only_attempts and row >= len(history):
            break  # Skip empty rows in the final grid if show_only_attempts is True

        row_display = " " * (padding - 2) + "| "  # Start row with padding and vertical border
        if row < len(history):
            guess, feedback = history[row]
            for i, color in enumerate(feedback):
                # Show letter only if show_letters is True, otherwise just display a blank cell
                letter = f" {guess[i]} " if show_letters else "   "
                if color == "green":
                    row_display += f"{green_bg}{letter.center(cell_width - 2)}{reset}{space_between_cells}"
                elif color == "yellow":
                    row_display += f"{yellow_bg}{letter.center(cell_width - 2)}{reset}{space_between_cells}"
                else:
                    row_display += f"{gray_bg}{letter.center(cell_width - 2)}{reset}{space_between_cells}"
            row_display = row_display.rstrip()  # Remove trailing space
            row_display += "|"
        else:
            # Display empty cells for unused attempts
            row_display += (f"{empty_cell.center(cell_width)}{space_between_cells}") * 5
            row_display = row_display.rstrip()  # Remove trailing space
            row_display += " |"
        print(row_display)
    print(" " * (padding - 2) + "+" + "-" * (row_content_width + 2) + "+")  # Bottom border
    print("\n")  # Extra space after the grid

def display_final_grid(history, correct_word, won, window_width=50):
    results_width = window_width - 4
    padding = (window_width - results_width) // 2

    # Top border of the results frame
    print(" " * padding + "+" + "-" * (results_width - 2) + "+")

    # Title line
    print(" " * padding + "| " + "RESULTS".center(results_width - 4) + " |")

    # Separator line
    print(" " * padding + "+" + "-" * (results_width - 2) + "+")

    if won:
        # Winning message
        print(" " * padding + "| " + "Congratulations!".center(results_width - 4) + " |")
        print(" " * padding + "| " + "You've found the correct word!".center(results_width - 4) + " |")
        print(" " * padding + "| " + f"Word: {correct_word}".center(results_width - 4) + " |")
        
        # Bottom message
        print(" " * padding + "+" + "-" * (results_width - 2) + "+")
        print(" " * padding + "| " + "Press any key to return to the menu.".center(results_width - 4) + " |")
        print(" " * padding + "+" + "-" * (results_width - 2) + "+")
    else:
        # Losing message with the correct word and full grid display
        print(" " * padding + "| " + "Game Over! Better luck next time.".center(results_width - 4) + " |")
        print(" " * padding + "| " + f"The correct word was: {correct_word.upper()}".center(results_width - 4) + " |")

        # Padding before the grid to vertically center it
        for _ in range(2):
            print(" " * padding + "| " + " " * (results_width - 4) + " |")

        # Display the full grid for the losing screen
        cell_width = 5
        grid_content_width = (cell_width * 5) + 5
        grid_padding = (results_width - grid_content_width - 4) // 2
        right_shift_padding = 7

        for row in range(6):
            row_display = " " * padding + "| " + " " * (grid_padding + right_shift_padding)
            if row < len(history):
                _, feedback = history[row]
                for color in feedback:
                    if color == "green":
                        row_display += f"{GREEN}{' ' * (cell_width - 2)}{RESET}"
                    elif color == "yellow":
                        row_display += f"{YELLOW}{' ' * (cell_width - 2)}{RESET}"
                    else:
                        row_display += f"{GRAY}{' ' * (cell_width - 2)}{RESET}"
                row_display += " " * grid_padding + "         |" 
            else:
                row_display += ("⬛" * 5).center(grid_content_width) + " " * grid_padding + " |"
            print(row_display)

        # Padding after the grid
        for _ in range(2):
            print(" " * padding + "| " + " " * (results_width - 4) + " |")

        # Bottom message and border
        print(" " * padding + "+" + "-" * (results_width - 2) + "+")
        print(" " * padding + "| " + "Press any key to return to the menu.".center(results_width - 4) + " |")
        print(" " * padding + "+" + "-" * (results_width - 2) + "+")
    input("Enter command: ")


def start_game(difficulty):
    correct_word = random.choice(difficulties[difficulty]["WORDS"])
    max_attempts = 6
    window_width = 50

    attempts = 0
    won = False
    history = []  # To store previous guesses and feedback

    while attempts < max_attempts:
        clear_screen()
        print("+" + "-" * (window_width - 2) + "+")
        print("|" + center_text("GAME PAGE") + "|")
        print("+" + "-" * (window_width - 2) + "+")

        # Display the current grid based on history
        display_wordle_grid(history)
        
        print(f"|{center_text(f'Attempt {attempts + 1}/{max_attempts}')}|")
        print("|" + center_text("Type your 5-letter guess below:") + "|")
        print("+" + "-" * (window_width - 2) + "+")
        
        guess = input("Your Guess: ").upper()
        
        if len(guess) != 5 or not guess.isalpha():
            print(utils.COLORS["RED"] + "Please enter a valid 5-letter word." + utils.COLORS["RESET"])
            input(utils.COLORS["RED"] + "Press any key to try again." + utils.COLORS["RESET"])
            continue

        # Generate feedback for the current guess
        feedback = []
        for i in range(5):
            if guess[i] == correct_word[i]:
                feedback.append("green")  # Correct position
            elif guess[i] in correct_word:
                feedback.append("yellow")  # Incorrect position
            else:
                feedback.append("gray")  # Not in word
        
        # Store current guess and feedback in history
        history.append((guess, feedback))
        
        # Check if user guessed correctly
        attempts += 1
        if guess == correct_word:
            won = True
            break

    utils.clear_console()
    display_final_grid(history, correct_word=correct_word, won=won)

    if won :
        return 1
    else:
        return -1
    
# Main function to display menu and handle user input
def main(difficulty):
    display_splash_screen()
    while True:
        utils.clear_console()
        display_menu()
        choice = input("Select an option: ")

        if choice == "1":
            print("Exiting the game...")
            break
        elif choice == "2":
            return start_game(difficulty)
        elif choice == "3":
            display_rules()
        else:
            print("Invalid option. Please try again.")
            input("Press any key to continue...")

# Start the game
