#You should pick good names for your variables.
#You do not have to perform the entire computation in one line; you can use multiple lines to perform the computation if you want.
#It is OK to introduce variables to hold values that are not a “final” value. For example, if you were computing the area of a circle, you might store the radius in one variable, then the radius squared in another variable, and then later multiply that by pi to compute the area.

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: Lab 2.9
# Date: 1 September 2023

from math import *

#calculations
force = 27*1.5
wavelength = (2*0.025*sin(radians(35)))
radon = 27 * pow(2,-5/3.8)
pressure = (5*415*8.314)/0.27

#printing calculations
print("Force is {} N".format(force))
print("Wavelength is {} nm".format(wavelength))
print("Radon-222 left is {} g".format(radon))
print("Pressure is {} kPa".format(pressure/1000))
