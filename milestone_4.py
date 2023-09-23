import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        # Convert the guessed letter to lower case
        guess = guess.lower()
        
        if guess in self.word:
            self.reveal_letter(guess)
        else:
            self.reduce_life(guess)
    
    def reveal_letter(self, guess):
        print(f"Good guess! {guess} is in the word.")
        for index, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[index] = guess
        self.num_letters -= 1
    
    def reduce_life(self, guess):
        self.num_lives -= 1
        print(f"Sorry, {guess} is not in the word.")
        print(f"You have {self.num_lives} lives left.")
    
    def ask_for_input(self):
        while True:
            guess = input("Please, guess a letter: ").strip().lower()
            
            if self.is_invalid_guess(guess):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
                break
                
    def is_invalid_guess(self, guess):
        return not guess.isalpha() or len(guess) != 1


if __name__ == "__main__":
    word_list = ["apple", "banana", "cherry"]
    game = Hangman(word_list)
    game.ask_for_input()
    print("List of guesses:", game.list_of_guesses)
    print("Word Guessed so far:", ''.join(game.word_guessed))
