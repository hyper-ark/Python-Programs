# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: Lab 4.16 Largest Number
# Date: 13 September 2023

#take inputs
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))

largest_number = 0.0

#determine largest
if num1>num2 and num1>num3:
    largest_number = num1
elif num2>num1 and num2>num3:
    largest_number = num2
else:
    largest_number = num3

print("The largest number is", largest_number)
    