#Write a python program named guessing_game.py to play a number guessing game. Have your program display a short message with instructions, then continually prompt the user to guess a number. With each wrong guess, let the user know if their guess is too high or too low. When the user correctly guesses the number, output the total number of valid guesses made. Write your program using at least two (2) functions and a try-except statement. 

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: Lab 10.15
# Date: 2 11 2023

#sees if guess is higher or lower
def guess_val(n):
    if n < secret_num:
        print("Too low!")
    elif n > secret_num:
        print("Too high!")

#sees if guess input is valid
def valid_input(guess):
    try:
        guess = int(guess)
    except ValueError:
        return False
    return True
        
print("Guess the secret number! Hint: it's an integer between 1 and 100...")
secret_num = 27
guess = ""
guesses = 0

#loop for user to guess secret number
while guess != secret_num:
    
    guess = input("What is your guess? ")
    while valid_input(guess) == False:
        guess = input("Bad input! Try again: ")
    else:
        guess = int(guess)
        guess_val(guess)
        guesses += 1
    
else:
    print(f"You guessed it! It took you {guesses} guesses.")
