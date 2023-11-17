#Write a program named howdy_whoop.py that takes as input from the user two positive integers. Output the numbers 1 to 100, each on its own line, unless the number is evenly divisible by one or both of the integers entered by the user. If the number is evenly divisible by the first integer, print Howdy. If it’s evenly divisible by the second integer, print Whoop. If it’s evenly divisible by both, print Howdy Whoop.

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: Lab 6.13 Howdy Whoop
# Date: 29 September 2023

#inputs
int1 = int(input("Enter an integer: "))
int2 = int(input("Enter another integer: "))
count = 1

while count != 101:
    divis1 = count%int1 == 0
    divis2 = count%int2 == 0
    if divis1 and divis2:
        print("Howdy Whoop")
    elif divis1 and not divis2:
        print("Howdy")
    elif divis2 and not divis1:
        print("Whoop")
    else:
        print(count)
    count += 1
    
