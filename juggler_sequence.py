# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: Lab 6.15 Juggler sequence
# Date: 29 September 2023

num = int(input("Enter a positive integer: "))
print(f"The Juggler sequence starting at {num} is:")
count = 0
#sequence
while num != 1:
    print(num, end = ', ')
    if num%2 == 0:
        num = int(num**0.5)
    else:
        num = int(num**1.5)
    count += 1
    
print(num)
print(f"It took {count} iterations to reach 1")
