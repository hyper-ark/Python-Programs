#Write a program named boolean_expressions.py that takes as input from the user Boolean values from the keyboard for variables a, b, and c. The program should also evaluate the following Boolean expressions using the variables a, b, and c. Use Boolean expressions; do NOT use if-elif-else blocks.

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Yuqing Cao
# Pooja Marella
# Arya Kumar
# Nicolaus Reali
# Section: 514
# Assignment: boolean_expressions – team
# Date: 12/9/2023

############ Part A ############
a=input("Enter True or False for a: ")
b=input("Enter True or False for b: ")
c=input("Enter True or False for c: ")

if a=="True" or a=="t" or a=="T":
    a=True
elif a=="False" or a=="f" or a=="F":
    a=False

if b=="True" or b=="t" or b=="T":
    b=True
elif b=="False" or b=="f" or b=="F":
    b=False

if c=="True" or c=="t" or c=="T":
    c=True
elif c=="False" or c=="f" or c=="F":
    c=False

############ Part B ############
print("a and b and c:", a and b and c)
print("a or b or c:",a or b or c)

############ Part C ############
print("XOR:",not (a == b))
print("Odd number:",(a or b or c) and not(a and b and not(c)) and not(a and c and not(b)) and not(b and c and not(a)))

############ Part D ############
Complex1=(not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
Complex2=(not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b
and c) or (a and ((b and not c) or (not b))))

Simplified1=((b and not(a and c))) and (not b) or (not(a and b or c)) or (a and not b)
Simplified2=(a and not c) and (not a or (a and (b and c)) or (a and (not b or not c)))

print("Complex 1:",Complex1)
print("Complex 2:",Complex2)
print("Simple 1:", Simplified1)
print("Simple 2:", Simplified2)
