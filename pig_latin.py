#Write a program named pig_latin.py that takes as input from the user one string containing multiple words each separated by a single space. Have your program convert the words to Pig Latin, then print both the original words and Pig Latin versions using the format shown below.

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: Lab 7.25 Pig latin
# Date: 4 October 2023

user_input = input("Enter word(s) to convert to Pig Latin: ")
words = user_input.split(" ")
for word in words:
    if word[0] in ['a','e','i','o','u','y']:
        words[words.index(word)] = word + "yay"
    else:
        new_word = word
        while new_word[0] not in ['a','e','i','o','u','y']:
            new_word = new_word[1:] + new_word[0]
        words[words.index(word)] = new_word + "ay"
        
#print
output = " ".join(words)
print(f'In Pig Latin, "{user_input}" is: {output}')
        
