while True:
    guess = input("Guess a letter: ")
    if guess.isalpha == len(guess):
        break # break out of the loop
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
    if guess in len(guess):
        print("Good guess! {guess} is in the word")
    else:
        print("Sorry, {guess} is not in the word. Try again")

# Step 1: Define the check_guess function
def check_guess(guess, word):
    # Step 2: Convert the guess to lower case
    guess = guess.lower()
    
    # Step 3: Check if the guess is in the word
    if guess in word:
        return True
    else:
        return False

# Step 1: Define the ask_for_input function
def ask_for_input(word):
    # Step 2: Move the input validation code here
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
        else:
            break

    # Step 3: Call the check_guess function to check if the guess is in the word
    if check_guess(guess, word):
        print(f"{guess} is in the word!")
    else:
        print(f"{guess} is not in the word.")

# Step 4: Call the ask_for_input function to test the code
word = "example"  # Replace with your word
ask_for_input(word)

