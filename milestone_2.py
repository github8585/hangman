import random

word_list = ['orange', 'apple', 'pear', 'banana', 'kiwi']
print(word_list)

word = random.choice(word_list)

print(word)

guess = input("Enter a letter: ")

if guess in word == len.word:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")




