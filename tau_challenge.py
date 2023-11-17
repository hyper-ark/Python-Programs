#Using only the commands we have covered in class so far, write a program named tau_challenge.py that asks a user for a number of digits, and prints the number tau rounded to that many digits of precision. Do NOT use the round() function. Instead, get creative and think of another way!

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: Lab 3.18 Writing Functions
# Date: 8 September 2023

from math import *

precision = int(input("Please enter the number of digits of precision for tau: "))
result = f"{tau*10**precision:.0f}"
print(f"The value of tau to {precision} digits is: {int(result)/10**precision}")
