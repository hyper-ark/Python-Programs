#Convert your using_variables.py program to a new program named using_input.py that produces identical output. However, your new program should take in input from the user as appropriate, store values in variables, and output in the required format.

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: Lab 3.17 Using Input
# Date: 8 September 2023

from math import *

#Force
print("This program calculates the applied force given mass and acceleration")
mass = float(input("Please enter the mass (kg): "))
acceleration = float(input("Please enter the acceleration (m/s^2): "))
print(f"Force is {mass*acceleration:.1f} N")

#Wavelength
print("This program calculates the wavelength given distance and angle")
distance = float(input("Please enter the distance (nm): "))
angle = float(input("Please enter the angle (degrees): "))
print(f"Wavelength is {2*distance*sin(radians(angle)):.4f} nm")

#Radon
print("This program calculates how much Radon-222 is left given time and initial amount")
time = float(input("Please enter the time (days): "))
amount = float(input("Please enter the initial amount (g): "))
print(f"Radon-222 left is {amount * pow(2,-time/3.8):.2f} g")

#Pressure
print("This program calculates the pressure given moles, volume, and temperature")
moles = float(input("Please enter the number of moles: "))
volume = float(input("Please enter the volume (m^3): "))
temperature = float(input("Please enter the temperature (K): "))
print(f"Pressure is {((moles*8.314*temperature)/volume)/1000:.0f} kPa")
