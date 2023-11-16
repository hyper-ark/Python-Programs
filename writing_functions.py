# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: Lab 3.18 Writing Functions
# Date: 8 September 2023

from math import *

#functions
def triangle (s):
    return (sqrt(3)/4*s**2)

def square(s):
    return s**2

def pentagon(s):
    return(0.25*sqrt(5*(5+2*sqrt(5)))*s**2)

def dodecagon(s):
    return(3*(2+sqrt(3))*s**2)

#input and prints
side = float(input("Please enter the side length: "))
print(f"A triangle with side {side:.2f} has area {triangle(side):.3f}")
print(f"A square with side {side:.2f} has area {square(side):.3f}")
print(f"A pentagon with side {side:.2f} has area {pentagon(side):.3f}")
print(f"A dodecagon with side {side:.2f} has area {dodecagon(side):.3f}")