# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: Lab 4.19 Calculate roots
# Date: 14 September 2023

from math import *

#taking inputs
a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))

if a == 0 and b == 0 and c != 0:
    print("You entered an invalid combination of coefficients!")
    
elif a == 0 and b != 0 and c != 0:
    print("The root is x =", -c/b)
    
else:
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        
        real_part = -b/(2*a)
        imaginary_part = str(sqrt(-discriminant)/(2*a)) + 'i'
        root_one = f"{real_part} + {imaginary_part}"
        root_two = f"{real_part} - {imaginary_part}"
        
        if sqrt(-discriminant)/(2*a) < 0:
            larger_root = root_two
            smaller_root = root_one
        else:
            larger_root = root_one
            smaller_root = root_two
            
    else:
        
        root_one = (-b + sqrt(discriminant)) / (2*a)
        root_two = (-b - sqrt(discriminant)) / (2*a)
        
        if root_one > root_two:
            larger_root = root_one
            smaller_root = root_two
        else:
            larger_root = root_two
            smaller_root = root_one
        
    if root_one == root_two:
        print(f"The root is x = {root_one}")
    else:
        print(f"The roots are x = {larger_root} and x = {smaller_root}")
    
   
