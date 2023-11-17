#Write a program named still_more_linear_interpolation.py that takes as input the time and location of a moving object at two points, then using linear interpolation calculates the position at several intermediate times. Your program needs to prompt the user to enter the time and position at two points, calculate the times and positions for five evenly spaced points, and print the results using nice formatting. Display the times using two (2) decimal places and the positions using three (3) decimal places.

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Yuqing Cao
# Pooja Marella
# Arya Kumar
# Nicolaus Reali
# Section: 514
# Assignment: still more linear interpolation – team
# Date: 1/9/2023

from math import*

#variables
t1 = float(input("Enter time 1: "))
x1 = float(input("Enter the x position of the object at time 1: "))
y1 = float(input("Enter the y position of the object at time 1: "))
z1 = float(input("Enter the z position of the object at time 1: "))
t2 = float(input("Enter time 2: "))
x2 = float(input("Enter the x position of the object at time 2: "))
y2 = float(input("Enter the y position of the object at time 2: "))
z2 = float(input("Enter the z position of the object at time 2: "))

#calculations
slope_x1 = (x2-x1)/(t2-t1)
slope_y1 = (y2-y1)/(t2-t1)
slope_z1 = (z2-z1)/(t2-t1)

t=t1
f_x1=(slope_x1)*(t-t1)+x1
f_y1=(slope_y1)*(t-t1)+y1
f_z1=(slope_z1)*(t-t1)+z1
print(f'At time {t:.2f} seconds the object is at ({f_x1:.3f}, {f_y1:.3f}, {f_z1:.3f})')

t=(t2-t1)/4+t1
f_x1=(slope_x1)*(t-t1)+x1
f_y1=(slope_y1)*(t-t1)+y1
f_z1=(slope_z1)*(t-t1)+z1
print(f'At time {t:.2f} seconds the object is at ({f_x1:.3f}, {f_y1:.3f}, {f_z1:.3f})')

t=(t2-t1)/4*2+t1
f_x1=(slope_x1)*(t-t1)+x1
f_y1=(slope_y1)*(t-t1)+y1
f_z1=(slope_z1)*(t-t1)+z1
print(f'At time {t:.2f} seconds the object is at ({f_x1:.3f}, {f_y1:.3f}, {f_z1:.3f})')

t=(t2-t1)/4*3+t1
f_x1=(slope_x1)*(t-t1)+x1
f_y1=(slope_y1)*(t-t1)+y1
f_z1=(slope_z1)*(t-t1)+z1
print(f'At time {t:.2f} seconds the object is at ({f_x1:.3f}, {f_y1:.3f}, {f_z1:.3f})')

t=t2
f_x1=(slope_x1)*(t-t1)+x1
f_y1=(slope_y1)*(t-t1)+y1
f_z1=(slope_z1)*(t-t1)+z1
print(f'At time {t:.2f} seconds the object is at ({f_x1:.3f}, {f_y1:.3f}, {f_z1:.3f})')
