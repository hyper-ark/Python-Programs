# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: Lab 5.4 Boiling curve
# Date: 22 September 2023

#import library
from math import *

#taking input from user for excess temperature
x = float(input("Enter the excess temperature: "))

#initialize points for line segments
x0 = 0      #line segment first 'x' value
x1 = 0      #line segment second 'x' value
y0 = 0      #line segment first 'y' value
y1 = 0      #line segment second 'y' value

#use conditionals to determine which line segment inputted excess temperatrure falls on
if x < 1.3 or x > 1200:     #if 'x' is out of range
    print("Surface heat flux is not available")
else:
    if x >= 1.3 and x < 5:        #first line segment
        x0 = 1.3
        x1 = 5
        y0 = 1000
        y1 = 7000
        
    elif x >= 5 and x < 30:         #second line segment
        x0 = 5
        x1 = 30
        y0 = 7000
        y1 = 1500000
        
    elif x >= 30 and x < 120:       #third line segment
        x0 = 30
        x1 = 120
        y0 = 1500000
        y1 = 25000
    
    elif x >= 120 and x < 1200:     #fourth line segment
        x0 = 120
        x1 = 1200
        y0 = 25000
        y1 = 1500000
    
    #slope calculation
    m = (log10(y1 / y0))/(log10(x1 / x0))
    #surface heat flux calculation
    y = y0 * ((x / x0) ** m)
    #formatted output for surface heat flux
    print(f"The surface heat flux is approximately {y:.0f} W/m^2")


