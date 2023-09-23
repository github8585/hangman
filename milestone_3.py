def is_letter_in_word(letter, word):
    letter = letter.lower()
    return letter in word

def get_validated_user_input():
    while True:
        user_input = input("Guess a letter: ").lower()
        if len(user_input) == 1 and user_input.isalpha():
            return user_input
        else:
            print("Please enter a single alphabetical character.")

def play_guessing_game(target_word):
    while True:
        guessed_letter = get_validated_user_input()
        if is_letter_in_word(guessed_letter, target_word):
            print(f"Good guess! {guessed_letter} is in the word.")
        else:
            print(f"Sorry, {guessed_letter} is not in the word. Try again.")

if __name__ == "__main__":
    word_to_guess = "example"
    play_guessing_game(word_to_guess)
