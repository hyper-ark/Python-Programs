#Write a program named leet_speak.py that takes as input from the user a string of text, converts the words to leet, and prints the converted text. Your program must use a dictionary.

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: Lab 7.26 Leet speak
# Date: 4 October 2023

user_input = input("Enter some text: ")
leet = {'a':4,'e':3,'o':0,'s':5,'t':7}
text = user_input

#key iteration
for key in leet:
    text = text.replace(key,str(leet[key]))

print(f'In leet speak, "{user_input}" is:\n{text}')    
        
        
