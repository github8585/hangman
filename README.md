Python-Based Hangman Console Game
Project Synopsis:
This repository houses a Python implementation of the classic game, Hangman. It’s a text-centric interface where users interact and guess the concealed word, one letter at a time, under a limited allowance of incorrect guesses.

Instructions for Engagement:
Upon initiation, the program selects a word at random from a predefined catalog of words.
Users are sequentially prompted to posit a letter as their guess.
Should the letter exist within the word, its locations are unmasked.
Conversely, should the guess be incorrect, the user loses one of their finite lives.
Victory is achieved by unveiling the entire word within the allocated lives; otherwise, a defeat is declared.
Architectural Overview:
The underlying architecture of this game orbits around a central Python class, named Hangman. This class is the custodian of the game’s status and encapsulates methods to validate guesses and render the prevailing game state. The execution commences with the play_game function, initializing a game instance and managing the game sequence. The pivotal methods within the Hangman class encompass check_guess, ask_for_input, is_game_over, has_won, and display_game_state.

Execution Procedure:
To immerse in the game, launch the Python script via the terminal or command interface with the command python3 scriptname.py, substituting scriptname with the genuine name of your script file.

Vocabulary Catalog:
The inherent vocabulary catalog encapsulates the words 'apple', 'banana', and 'cherry'. This catalog is adaptable and can be configured to integrate any assortment of words as per preference.

Participation and Contributions:
Contributions to the enhancement of this project are highly welcomed. For substantial modifications or enhancements, kindly initialize a discussion by opening an issue before making any pull requests.

Feel free to adapt it more to fit any other specific information or styling you prefer!
