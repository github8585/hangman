import random


class Hangman:
    def __init__(self, word_list: list[str], num_lives: int = 5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.num_letters = len(set(self.word))

    def check_guess(self, guess: str) -> None:
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess

            self.num_letters -= 1
        else:
            # Handling incorrect guesses
            self.num_lives -= 1  # Reducing num_lives by 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self) -> None:
        while True:
            guess = input("Please, guess a letter: ").strip().lower()

            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
    
    def is_game_over(self) -> bool:
        return self.num_lives == 0
    
    def has_won(self) -> bool:
        return self.num_letters == 0
    
    def display_game_state(self) -> None:
        print(' '.join(self.word_guessed))
        print("List of guesses:", ', '.join(self.list_of_guesses))
        print(f"You have {self.num_lives} lives left.\n")


def play_game(word_list: list[str]) -> None:
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        game.display_game_state()

        if game.is_game_over():
            print(f'You lost! The word was {game.word}.')
            break
        elif not game.has_won():
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break


if __name__ == "__main__":
    word_list = ['apple', 'banana', 'cherry']
    play_game(word_list)
