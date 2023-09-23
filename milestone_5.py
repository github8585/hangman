class Hangman:
    def __init__(self, word_list, num_lives):
        # Assuming your Hangman class has an initializer that takes a word list and num_lives as parameters
        pass  # Replace with the actual code
    
    def ask_for_input(self):
        # Assuming this is a method that handles user input and game logic
        pass  # Replace with the actual code
    
    # Add other methods if necessary


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    num_letters = 1  # Initialize with a value greater than 0 to start the game loop
    
    while True:
        if num_lives == 0:
            print('You lost!')
            break  # Exit the loop
        elif num_letters > 0:
            game.ask_for_input()  # Assuming this method will also update num_lives and num_letters accordingly
        else:
            print('Congratulations. You won the game!')
            break  # Exit the loop

    # Optionally, add a replay feature here if you want
        

# Replace with your actual word list
word_list = ['apple', 'banana', 'cherry']
play_game(word_list)
