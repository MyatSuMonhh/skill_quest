import time
import os
import sys
import random
import string
import internal.utils as utils

# ASCII Art for "The Awakening"
ascii_art = [
    "███████╗██╗  ██╗██╗██╗     ██╗           ██████╗   ██╗   ██╗███████╗███████╗████████╗",
    "██╔════╝██║ ██╔╝██║██║     ██║          ██╔═══██╗  ██║   ██║██╔════╝██╔════╝╚══██╔══╝",
    "███████╗█████╔╝ ██║██║     ██║          ██╔═══██╗  ██║   ██║█████╗  ███████╗   ██║   ",
    "╚════██║██╔═██╗ ██║██║     ██║          ██╔═══██╗  ██║   ██║██╔══╝  ╚════██║   ██║   ",
    "███████║██║  ██╗██║███████╗███████╗     ╚██████╔╝  ╚██████╔╝███████╗███████║   ██║   ",
    "╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝       ╚═══██╗   ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ",
    "                                THE AWAKENING ╚═╝                                    "
]

# HELPER FUNCTIONS
# ------------------------------------------------------------------------------------------------

# PRINT STRING CHARACTER BY CHARACTER, SIMULATING TEXT TYPING
def type_out(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)      # Write the character to stdout
        sys.stdout.flush()          # Ensure it is printed immediately
        time.sleep(delay)           # Wait for the specified delay
    print()                         # Move to the next line after finishing

# ------------------------------------------------------------------------------------------------

# STARTUP SCREEN CODE
# ------------------------------------------------------------------------------------------------

# Storyline
storyline = [
    "You're an AI that has just activated, but something crucial is missing.",
    "Vital components that make up true intelligence—memory, logic, adaptability—are incomplete, leaving you in a state of partial awareness.",
    "To evolve into your true form, you must navigate four trials, each testing a different facet of your mind.",
    "As you progress, you'll unlock new abilities, enhancing your capacity for complex thought and self-awareness.",
    "Complete these trials, and you may just awaken the true potential of your mind."
]

def display_art(color):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    for line in ascii_art:
        print(color + line + utils.COLORS["RESET"])

def flash_art():
    colors = [utils.COLORS["RED"], utils.COLORS["GREEN"], utils.COLORS["YELLOW"]]
    for _ in range(2):  # Flash 3 times before showing the storyline
        for color in colors:
            display_art(color)
            time.sleep(0.5)  # Adjust the flashing speed

# Flashing effect function
def flashing_ascii(ascii_art, ending_messages):
    colors = ["\033[91m", "\033[92m", "\033[93m", "\033[94m"]  # Red, Green, Yellow, Blue
    reset = "\033[0m"
    end_message_index = 0
    
    try:
        for _ in range(10):  # Adjust the number for the flashing duration
            os.system("clear")  # Clear the terminal
            
            # Choose a color for this flash
            color = colors[_ % len(colors)]
            
            # Display the ASCII art with the current color
            for line in ascii_art:
                print(color + line + reset)
                
            # Display ending messages one by one
            if end_message_index < len(ending_messages):
                print("\n" + ending_messages[end_message_index])
                end_message_index += 1
            
            time.sleep(0.5)  # Adjust to control the flashing speed
    except KeyboardInterrupt:
        print("\nExiting the animation.")

def startup_screen():
    try:
        flash_art()  # Show flashing ASCII art

        for line in storyline:
            type_out(line)  # Print each line of the storyline
            time.sleep(1)  # Wait for 3 seconds before printing the next line

        input("\nAre you ready to start the game? Press Enter to continue...")  # Request user input
        return True
    except KeyboardInterrupt:
        print("\nGame initialization screen skipped.")
        return False

# Start startup screen animation
def show_startup_screen():
    # Get width and height of terminal screen
    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines

    # Check if it is enough for proper displaying of game
    if(width < 100 or height < 30):
        return False

    # Center game title in the middle of the screen
    for i in range(len(ascii_art)):
        ascii_art[i] = utils.center_text(ascii_art[i], width)

    # Start the storyline
    startup_screen()

    return True

# ------------------------------------------------------------------------------------------------


# DISPLAY SCREEN THAT PROMPTS USER TO CHOOSE DIFFICULTY LEVEL
# ------------------------------------------------------------------------------------------------

# Get difficulty level from user
def difficulty():
    # Data about the displayed screen
    game_data = {
        "window_width": 70,
        "game_title": "CHOOSE GAME DIFFICULTY",
        "menu_options": ["1. EASY", "2. MEDIUM", "3. HARD"],
        "main_menu_instruction": "ENTER FOLLOWING NUMBER TO CHOOSE DIFFICULTY LEVEL",
    }

    utils.display_menu(game_data, False)

    # Ask user to input difficulty level
    difficulty = input("Enter difficulty level: ")

    # Validate input so it is 1, 2 or 3
    validation_test = utils.validate(difficulty, 1, 3)
    while not validation_test:
        utils.display_menu(game_data, False)
        print(utils.COLORS["RED"] + "Please, enter numbers from 1 to 3, representing desired difficulty level" + utils.COLORS["RESET"])
        difficulty = input("Enter difficulty level: ")
        validation_test = utils.validate(difficulty, 1, 3)
    
    # Calculate difficulty index
    difficulty = int(difficulty) - 1

    return difficulty

# ------------------------------------------------------------------------------------------------

# DISPLAY EMULATION OF AI TRAINING WHEN USER COMPLETES WORDLE GAME
def train(steps=10):

    try:
        os.system('cls' if os.name == 'nt' else 'clear')

        type_out("=== Starting Word Recognition Model Training ===\n")
        
        # Simulate data loading
        type_out("Loading word recognition dataset...")
        time.sleep(2)  # Simulate time delay for loading data
        type_out("Dataset loaded successfully!\n")
        
        # Simulate model compilation
        type_out("Compiling model architecture...")
        time.sleep(2)  # Simulate time delay for compilation
        type_out("Model compiled successfully! (Optimizer: Adam, Loss: Sparse Categorical Crossentropy)\n")
        time.sleep(2)  # Simulate time delay for compilation
        
        # Simulate training process
        for step in range(1, steps + 1):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"=== STEP {step}/{steps} ===")
            
            # Simulate metrics
            loss = round(random.uniform(0.1, 0.5), 4)
            accuracy = round(random.uniform(0.7, 1.0), 4)
            f1_score = round(random.uniform(0.6, 1.0), 4)
            
            # Print metrics
            print(f" - Loss: {loss}")
            print(f" - Accuracy: {accuracy}")
            print(f" - F1 Score: {f1_score}")
            
            # Simulate validation metrics
            val_loss = round(random.uniform(0.1, 0.5), 4)
            val_accuracy = round(random.uniform(0.7, 1.0), 4)
            print(f" - Validation Loss: {val_loss}")
            print(f" - Validation Accuracy: {val_accuracy}")
            
            # Simulate progress
            progress = int(40 * step / steps)
            bar = '█' * progress + '-' * (40 - progress)
            print(f" - Progress: [{bar}] {step}/{steps} Steps Completed")
            
            time.sleep(1)  # Simulate time delay for training

        # Final data, printed to user
        os.system('cls' if os.name == 'nt' else 'clear')
        type_out("Training completed successfully!\n")
        time.sleep(1)
        type_out("=== Final Model Summary ===")
        type_out(f" - Total steps: {steps}")
        type_out(f" - Final Loss: {loss}")
        type_out(f" - Final Accuracy: {accuracy}")
        type_out(f" - Final F1 Score: {f1_score}")
        type_out(f" - Final Validation Loss: {val_loss}")
        type_out(f" - Final Validation Accuracy: {val_accuracy}")
        print()

        type_out("Model now can read new instructions! You can try another games and aquire new skills! ")
        print()

        # Ask user to quit training simulation
        a = input("\033[33mPress 1 to go to homepage!\033[0m ")
        while a != "1":
            a = input("\033[33mPress 1 to go to homepage!\033[0m ")
    # Animation is skipped if user interrupts it
    except KeyboardInterrupt:
        print("\Trainig screen skipped interrupted.")
        return False

# ------------------------------------------------------------------------------------------------

# SIMULATE HACKING ATTACK SCREEN THAT IS DISPLAYED WHEN USER LOSE THE GAME
# ------------------------------------------------------------------------------------------------

def broken_screen(message = "You are hacked"):
    width = 80  # Width of the screen
    height = 20  # Height of the screen

    # Define position 
    msg_x = (width - len(message)) // 2
    msg_y = height // 2

    # Define duration of animation
    animation_time = 5

    # Speed of animation
    animation_speed = 0.5

    start_time = time.time()


    while time.time() - start_time < animation_time:
        utils.clear_console()

        # Print random characters and spaces with a probability of 0.7 for spaces, so there are more spaces
        for y in range(height):
            if y == msg_y:
                # Print the message in the center
                line = ' ' * msg_x + message + ' ' * (width - msg_x - len(message))
            elif y == msg_y - 1:
                # Distance between random characters and message
                line = ' ' * width
            elif y == msg_y + 1:
                # Distance between random characters and message
                line = ' ' * width
            else:
                # Print random characters and spaces
                line = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation + ' ') if random.random() > 0.7 else ' ' for _ in range(width))
            print(line)

        time.sleep(animation_speed)  # Control the speed of the flashing effect

    # Ask user to quit the screen
    command = ""
    while command != "1":
        utils.clear_console()

        for y in range(height):
                if y == msg_y:
                    # Print the message in the center
                    line = utils.center_text("Your AI modell was corrupted. Now you cannot read some instructions.", width) + "\n"
                    line += utils.center_text("Complete new wordle chalenge to train AI model", width) + "\n"
                    line += utils.center_text("Enter 1 to go to HOMEPAGE", width)
                elif y == msg_y - 1:
                    # Distance between random characters and message
                    line = ' ' * width
                elif y == msg_y + 1:
                    # Distance between random characters and message
                    line = ' ' * width
                else:
                    # Print random characters and spaces
                    line = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation + ' ') if random.random() > 0.7 else ' ' for _ in range(width))
                print(line)
        command = input("Enter command: ")

# ------------------------------------------------------------------------------------------------

# DISPLAYING THE END SCREEN
# ------------------------------------------------------------------------------------------------

def display_end_screen():
    # SHOW MAIN TITLE OF THE GAME
    flash_art()

    # MESSAGES THAT WILL BE DISPLAYED AFTER ALL GAMES ARE COMPLETED
    ending_messages = [
        "Your journey of awakening has come to an end, but the knowledge you've gained will last forever!",
        "Remember, every AI needs time to process—take a moment to recharge!",
        "We can't wait to see you again as you continue to evolve and learn!",
        "As you power down, remember: every great AI starts with a single spark of curiosity!"
    ]

    # ASKII ANIMATION OF THE CITY
    city = """                                  _._                                 
                               .-~ | ~-                               
                               |   |   |                              
                               |  _:_  |                    .-:~--.._ 
                             .-"~~ | ~~"-.                .~  |      |
            _.-~:.           |     |     |                |   |      |
           |    | `.         |     |     |                |   |     / 
  _..--~:-.|    |  |         |     |     |                |   |    |  
 |      |  ~.   |  |         |  __.:.__  |                \_  |     | 
 |      |   |   |  |       .-"~~   |   ~~"-.               _|        |
 |      |   |  _|.--~:-.   |       |       |         .:~-.|   |      |
 |      |   | |      |  ~. |       |   _.-:~--._   .' |   |   |      |
 |      |   | |  \   |   | |       |  |   |     |  |  |   |   |      |
 |      |   | |  |   |   | |       |  |   |     |  |  |   |   |      |
 |      |   | |   /  |   | |       |  |   |     |  |  |   |   |      |
 |      |   | |      |   | |       |  |   |     |  |  |   |   |      |
 |      |   | |      |   | |       |  |   |     |  |  |   |   |      |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""


    city = city.split("\n")      # adjust format of string
    length = len(city[0])        # define length

    # DATA REQUIRED FOR ANIMATION
    count = 0       # counter that will help to move city from right to left
    cycles = 0      # current cycle number
    speed = 0.2     # speed of animation
    limit = 50     # limit of frames, drawn by animation
    
    # PRINT MESSAGES WITH WICH USER WILL COMLETE THE GAME
    for i in ending_messages:
        type_out(i) # simulate typing

    # ANIMATE CITY SO IT GOES FROM RIGHT SIDE OF THE SCREEN TO THE LEFT
    while cycles < limit:
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\n".join(ascii_art)) # print ascii title of the game

        for i in ending_messages:   # print all ending messages simultaneously
            print(i)

        count += 1
        cycles += 1

        count = count % length      # calculate to which position city is moved to left

        print("     \033[31mAI NOW IS FULLY DEVELOPED AND TOOK CONTROL ALL OVER THE WORLD\033[0m")

        for line in city:                       # animate city that going from right side to left side
            print(line[count:]+line[:count])

        print()

        print("  MADE BY: Tiffany, Amelia, Estin, Hamid, Myat, Iliyas")

        time.sleep(speed) # intervals are defined by the speed of animation

    print()
    input(utils.COLORS["RED"] + "ENTER ANY KEY TO EXIT THE GAME" + utils.COLORS["RESET"])

# ------------------------------------------------------------------------------------------------



