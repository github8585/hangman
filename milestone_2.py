import random

available_words = ['orange', 'apple', 'pear', 'banana', 'kiwi']
print(available_words)

selected_word = random.choice(available_words)

print(selected_word)

guess = input("Enter a letter: ")

if guess in selected_word and len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")




