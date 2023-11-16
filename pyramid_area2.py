# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Yuqing Cao
# Pooja Marella
# Arya Kumar
# Nicolaus Reali
# Section: 514
# Assignment: pyramid_area2 – team
# Date: 22/9/2023

from math import*
s=float(input("Enter the side length in meters: "))
n=float(input("Enter the number of layers: "))

rec=((n*(n+1))/2)*3 #rec = number of rectangles on all three sides
side_area=rec*s**2
topArea=n**2*(sqrt(3)/4)*(s**2)
total=side_area+topArea

print(f'You need {total:.2f} m^2 of gold foil to cover the pyramid')