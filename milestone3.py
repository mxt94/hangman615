import random

def check_guess(guess, secret_word):
    guess = guess.lower()
    if guess in secret_word:
        print(f"Good Guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.") 

    return guess

while True:
    secret_word = "apple"

    guess = ask_for_input()
    check_guess(guess, secret_word)          