# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: Lab 6.14 Double factorial
# Date: 29 September 2023

def doublefactorial (n):    #function
    if n == 0:
        return 1
    else:
        num = n
        sum = 1
        while num > 0:
            sum *= num
            num -= 2
        return sum
            
    