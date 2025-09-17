Skill Quest: THE AWAKENING-Readme File
Skill Quest: THE AWAKENING is a game developed for the HKU ENGG1330 course by group G1-1: Baishev Iliyas, Hamidov Aghahamid, Lau Estin, Myat Su Mon, Wang Hanyu and Zhang Difei
Watch this video demonstration to gain a better understanding of how to play the game: https://www.youtube.com/watch?v=wYElem0Drlk


It is a game developed in Python programming language and uses a terminal as an output stream. The game aims to test multiple capabilities and skills of the player, including memory, logical thinking, deductive reasoning, and so on. To achieve that goal, the game introduced an interesting scenario of imagining that the player was an awakening AI that lacks several abilities and calls for passing the skill quests to restore a complete self. 

To start playing, go to the skill_quest folder in the terminal. Run main.py using the command "python main.py" in the terminal. If an error occurs during the run procedure, check if Python is installed. To check if Python is installed use the command "python --version", if the output is "Python 3.x.x" Python is installed, otherwise, go to https://www.python.org and follow the instructions to download the latest version of Python. Also, make sure to drag the terminal to full-screen size. 

Once you're in, you will see a flashing ASCII art displaying the name of our game. It is done by the display_art(color) function, which displays ASCII art in the specified color, creating a visual effect by changing the color each time it is called. The storyline pops up one by one, this feature is done by the sleep function imported from the time module. Then, you will have to choose from three difficulty levels. You can exit or select one of the four puzzle games: Wordle, Pinpoint, Sudoku, and Emoji. Each puzzle tests a different skill essential for becoming a true intelligence. Then, type the corresponding number to select a game. 


WORDLE 
Wordle is a game that tests your quick-guessing skills. As an AI, you must develop the ability to make rapid guesses for real-time decision-making.

First, select option number 3 to read the rules. The goal is to guess a five-letter word within six attempts.

* If a letter is in the correct spot, it turns green.
* If the letter is in the word but in the wrong spot, it turns yellow.
* If it isn’t in the word, it turns gray.

After knowing the rules, press any key to go back to the main menu and then press 2 to start the game.


PINPOINT
This game tests your deductive reasoning skills, essential for making decisions with incomplete information.

As usual, press number 3 to read the rules first. You’ll be given a clue and must guess a word based on it. If your guess is incorrect, you will receive another clue and a new chance to guess. Remember, you only have a total of 5 attempts to guess the correct word


SUDOKU
This is Sudoku, a game that tests your logical thinking skills—an essential trait for AI, as clear logic is crucial.

There are three difficulty levels, each with a different board size and number of lives. The easy level uses a 4x4 board and provides 3 lives. The hardest level features a 9x9 board with only 2 lives.

To win, fill in the blank slots so that each row, column, and group contains the numbers 1 through 4, 6, or 9, depending on the board size. Each invalid move costs you 1 life. If you have no valid moves to make or run out of lives, you lose the game.


EMOJI
This is the Emoji Game, which challenges the player’s memory—a key skill for AI, as memory enables learning, reasoning, and adaptation.

In this game, emojis are displayed with corresponding numbers for a few seconds before disappearing. Later, a single emoji will appear, and you will need to recall its number. The easy level features 9 emojis; harder levels increase to 12 and 15 emojis.

If you can identify the correct number within 3 attempts, you win!


TECHNICAL ASPECTS
Code Structure:
- Game logic is written in the main.py file
- games folder holds code for different puzzle games
- os
- time
- sys
- random
- string
- re
- copy

The project is divided into three main parts: main.py, the internal folder, and the games folder.

* main.py holds the core game logic and handles events for winning and losing games.
* The games folder contains the source code for each puzzle game. Each game includes a function that returns a result: 1 for a win, -1 for a loss, and 0 if the user exits the game.
* Finally, the internal folder contains shared code used across the game. Screen.py manages game events, including the startup screen, hacking attack, and the animated ending screen. Utils.py provides helper functions for displaying, formatting, and validating data.

This code structure makes it easy to expand the game by adding new puzzles to the games folder with the provided interfaces. Additionally, shared code can be reused across games, significantly reducing the time needed to implement new ones.


INNOVATION
Our game provides a single hub for developing various skills across multiple games, helping to sustain user engagement. The variety of games encourages players to spend more time on each activity, while unique mechanics focused on training AI to perform well in different games set our game apart from others, making the experience more engaging and dynamic.
