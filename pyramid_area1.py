#Write a program named pyramid_area1.py that will ask the user to input the length of one side of the prism (in meters) and the number of layers of the pyramid. Have your program calculate the total area of gold foil that is needed to cover the pyramid. Your program must use a loop, however you may NOT use lists, tuples, or dictionaries.

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Yuqing Cao
# Pooja Marella
# Arya Kumar
# Nicolaus Reali
# Section: 514
# Assignment: pyramid_area1 – team
# Date: 22/9/2023

from math import*
s=float(input("Enter the side length in meters: "))
n=int(input("Enter the number of layers: "))
total=0
for layer in range(1,n+1):
    triangle = layer ** 2 #triangle = number of triangles
    topArea=triangle*((sqrt(3)/4)*(s**2))-(((layer-1)**2)*((sqrt(3)/4)*(s**2)))
    side_area=((s**2))*(3*layer)
    total += topArea+side_area

print(f'You need {total:.2f} m^2 of gold foil to cover the pyramid')
