import os
import time
import games.wordle as wordle
import games.pinpoint as pinpoint
import games.emoji as emoji
import games.sudoku as sudoku
import internal.utils as utils
import internal.screen as screen

class Game():
    # INITIALIZATION OF GAME DATA
    def __init__(self, game_data, current_page = 0):
        #self.current_page = current_page
        #self.section = ""
        self.progress = 0                               # Represents number of games taht user completed
        self.completed = [False, False, False, False]   # Holds completion of games
        self.read = False                               # States wether user can read instructions of Pinpoint, Sudoku and Emoji games
        self.game_data = game_data                      #  Holds data that is displayed on the homepage menu
        self.difficulty = 0                             # Set the difficulty level that will be used in games
        self.menu_error = ""                            # Used to hold message of validation error of input command

    # SERVING GAME EVENTS
    def start(self):
        screen_test = screen.show_startup_screen() # Check if the screen is big enough so each askii art will be properly displayed

        # Ask user to adjust terminal to proper size
        if(not screen_test): 
            print("Your window is to small, please adjust the screen to at least 100 characters in width and 30 characters in height and restart the game")
            return

        # Ask user to choose difficulty level
        self.difficulty = screen.difficulty()

        # 
        running = True
        while(running):
            utils.display_menu(self.game_data, False)
            if(self.menu_error != ""):
                print(self.menu_error)
                self.menu_error = ""
            command = input("Enter command: ")
            running = self.serve(command)
        os.system('cls||clear')

    # SERVING INPUT COMMAND
    def serve(self, command):

        # SERVE GAME EXIT
        if(command == "1"):
            return False
        # SERVE WORDLE GAME
        if(command == "2"):
            res = wordle.main(self.difficulty)
            # ADD PROGRESS POINT IN CASE USER WON THE GAME AND ALLOW TO GO TO OTHER GAMES
            if(res == 1):
                self.change_progress(0, 1)
                screen.train() # Simulate training of AI model when user gets ability to read instructions of Pinpoint, Sudoku and Emoji games
                self.read = True # Unlock Pinpoint, Sudoku and Emoji games
        
        # SERVE PINPOINT GAME
        elif(command == "3"):
            
            # CIPER TEXT IN CASE IF READING ABILITY IS NOT OPENED YET
            result = pinpoint.start(not self.read, self.difficulty)
            
            #ADD PROGRESSION
            if(result == 1):
                self.change_progress(1, 1)

            # RANDOMLY GIVE AWAY ABILITY TO READ IN CASE USER LOST GAME
            elif(result == -1):
                if(utils.random_event(0.4)):
                    screen.broken_screen()
                    self.change_progress(0, -1)
                    self.read = False

        # SERVE SUDOKU
        elif(command == "4"):

            # CIPER TEXT IN CASE IF READING ABILITY IS NOT OPENED YET
            result = sudoku.start(not self.read, self.difficulty)

            #ADD PROGRESSION
            if(result == 1):
                self.change_progress(2, 1)

            # RANDOMLY GIVE AWAY ABILITY TO READ IN CASE USER LOST GAME
            elif(result == -1):
                if(utils.random_event(0.4)):
                    screen.broken_screen()
                    self.change_progress(0, -1)
                    self.read = False

        # SERVE EMOJI GAME
        elif(command == "5"):

            # CIPER TEXT IN CASE IF READING ABILITY IS NOT OPENED YET
            result = emoji.start(not self.read, self.difficulty)

            #ADD PROGRESSION
            if(result == 1):
                self.change_progress(3, 1)

            # RANDOMLY GIVE AWAY ABILITY TO READ IN CASE USER LOSE GAME
            elif(result == -1):
                if(utils.random_event(0.4)):
                    screen.broken_screen()
                    self.change_progress(0, -1)
                    self.read = False

        else:
            # Assign error message if user input is invalid
            self.menu_error = utils.COLORS["RED"] + "Please, enter number from 1 to 5" + utils.COLORS["RESET"]

        # SERVE THE ENDING OF THE GAME WHEN USER COMPLETED ALL THE GAMES
        if self.progress >= 4:
            screen.display_end_screen()
            return False

        return True
        
    # UPDATE PROGRESS BAR ACCORDING TO CHANGES MADE ON PROGRESS VARIABLE
    def update_progress(self):
        # There is diferent output as the last progress bar does not have space after it: "█]"
        if(self.progress < 4):
            self.game_data["extra_information"][1] = "[" + "█ "*(self.progress)*2 + "  "*(3-self.progress)*2 + "   " + "]"
            # Make progress bar green
            self.game_data["extra_information"][1] = utils.color_text(self.game_data["extra_information"][1], utils.COLORS["GREEN"])
        else:
            self.game_data["extra_information"][1] = "[" + "█ "*(self.progress - 1)*2 + "█ █]"
            # Make progress bar green
            self.game_data["extra_information"][1] = utils.color_text(self.game_data["extra_information"][1], utils.COLORS["GREEN"])

    # MAKE CHANGES TO PROGRESS
    # FUNCTIONS CAN TAKE POSITIVE AND NEGATIVE VARIABLES TO MAKE CHANGES OVER PROGRESS
    # FUNCTION CHANGES COLOR OF GAME NAMES IN MAIN MENU TO INDICATE COMPLETEION OF EACH GAME
    def change_progress(self, game, amount):
        # If game was nat completed previously, change the completed variable 
        if(not self.completed[game] and amount > 0):
            self.completed[game] = True
            # Make menu option of this game green
            self.game_data["menu_options"][game + 1] = utils.color_text(self.game_data["menu_options"][game + 1], utils.COLORS["GREEN"])
            if(self.progress + amount <= 6):
                self.progress += amount
            # Change displayed progress bar
            self.update_progress()
        # Take away ability to read and decrease progress bar
        elif(self.completed[game] and amount < 0):
            self.completed[game] = False
            # Reset the color of menu option of wordle game
            self.game_data["menu_options"][game + 1] = utils.color_text(self.game_data["menu_options"][game + 1], utils.COLORS["BLACK"])
            if(self.progress + amount >= 0):
                self.progress += amount
            # Change displayed progress bar
            self.update_progress()



def main():
    # DEFINE GAME VARIABLES
    # ----------------------------------------------------------------------------------

    # DEFINE WIDTH OF THE GAME SCREEN
    window_width = 70 

    # DEFINE TITLE OF THE GAME
    game_title = "SKILL QUEST"
    game_title = utils.color_text(game_title, utils.COLORS["RED"]) # SET COLOR OF TITLE

    # DEFINE MENU OPTIONS FOR MAIN SCREEN
    menu_options = ["1. EXIT", "2. WORDLE", "3. PINPOINT", "4. SUDOKU", "5. EMOJI"]
    menu_options = utils.adjust_length(menu_options) # ADJUST LENGTH OF EACH MENU OPTIONS SO EACH ELEMENT HAVE SAME LENGTH

    # DEFINE INSTRUCTION THAT IS DISPLAYED AT THE BOTTOM OF THE SCREEN
    main_menu_instruction = "TYPE NUMBER TO GO TO THE FOLOWING PAGE "

    # DEFINE PROGRESS BAR CAPTION COLORED IN GREEN
    progress_bar_text = "PROGRESS"
    progress_bar_text = utils.color_text(progress_bar_text, utils.COLORS["RED"])

    # DEFINE PROGRESS BAR
    progress_bar = "[               ]"
    progress_bar = utils.color_text(progress_bar, utils.COLORS["GREEN"])

    # ----------------------------------------------------------------------------------

    # STRUCTURIZE GAME VARIABLES INTO DICTIONARY FOR USAGE IN CLASS
    game_data = {
        "window_width": window_width,
        "game_title": game_title,
        "menu_options": menu_options,
        "main_menu_instruction": main_menu_instruction,
        "extra_information": [progress_bar_text, progress_bar],
    }

    # DEFINE GAME VARIBALE THAT HOLDS GAME LOGIC AND DATA
    game = Game(game_data)

    # RUN GAME
    game.start()

if __name__ == "__main__":
    main()


