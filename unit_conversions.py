#Write one program named unit_conversions.py that prompts the user to enter one number, stores it in an appropriately named variable, performs the necessary calculations, and outputs the results to the screen with proper labels and two (2) decimal places for each unit conversion listed below. Define your own function for each unit conversion to perform the calculations.

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Yuqing Cao
# Pooja Marella
# Arya Kumar
# Nicolaus Reali
# Section: 514
# Assignment: Lab unit conversions – team
# Date: 1/9/2023

from math import *

user_input = float(input("Please enter the quantity to be converted: "))

#conversion functions

def newtons_conversion(pf):
    newtons = pf * 4.4482216
    return newtons

def meters_conversion(meters):
    feet = meters * 3.28084
    return feet

def atmosphere_conversion(atm):
    kpa = atm * 101.325
    return kpa

def Watt_2_BTU(W):
    BTU_hour = W * 3.412141633
    return BTU_hour

def liters_second_conversion(liters_second):
    gallons_minute = liters_second / 3.785411784 * 60
    return gallons_minute

def fahrenheit_conversion(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

print(f'{user_input:.2f} pounds force is equivalent to {newtons_conversion(user_input):.2f} Newtons')
print(f'{user_input:.2f} meters is equivalent to {meters_conversion(user_input):.2f} feet')
print(f'{user_input:.2f} atmospheres is equivalent to {atmosphere_conversion (user_input):.2f} kilopascals')
print(f'{user_input:.2f} watts is equivalent to {Watt_2_BTU(user_input):.2f} BTU per hour')
print(f'{user_input:.2f} liters per second is equivalent to {liters_second_conversion(user_input):.2f} US gallons per minute')
print(f'{user_input:.2f} degrees Celsius is equivalent to {fahrenheit_conversion(user_input):.2f} degrees Fahrenheit')
