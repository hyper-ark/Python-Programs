#Part 1: Determines, for a time of 25 minutes, where the ISS will be (in terms of kilometers past Houston).
#Part 2: Add to your program to determine, for a time of 300 minutes, where the ISS will be (in terms of kilometers past Houston).

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Yuqing Cao
# Pooja Marella
# Arya Kumar
# Nicolaus Reali
# Section: 514
# Assignment: Sequential Algorithm – team
# Date: 30/8/2023

from math import*

y2=23027 #km
y1=2027 #km
x2=55 #minutes
x1=10 #minutes
slope = (y2-y1)/(x2-x1)

#part 1
t=25 #t is time in minutes
p=(slope)*(t-x1)+y1 #p is position in km

print("Part 1:","\nFor t=25 minutes, the position p =",p,"kilometers")

#part 2
t=300 #t is time in minutes
p=(slope)*(t-x1)+y1 #p is position in km
r=6745 #r is radius in km
c = 2*pi*r #c is circumference in km
p_f = p%c #p_f is the final position in km
print("Part 2:","\nFor t=300 minutes, the position p =",p_f,"kilometers")
