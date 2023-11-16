# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Yuqing Cao
# Pooja Marella
# Arya Kumar
# Nicolaus Reali
# Section: 514
# Assignment: pretty_equation – team
# Date: 8/9/2023

from math import*
a=int(input("Please enter the coefficient A: "))
b=int(input("Please enter the coefficient B: "))
c=int(input("Please enter the coefficient C: "))

#checks for a
if a==-1:
    term1="- x^2"
    if b>0:
        term1+= " + "
elif a<0:
    term1="- " + str(abs(a)) + "x^2"
    if b>0:
        term1+= " + "
elif a==0:
    term1=""
elif a==1:
    term1="x^2"
    if b>0:
        term1+= " + "
elif a>0:
    term1=str(a) + "x^2"
    if b>0:
        term1+= " + "
else:
    term1=''
#checks for b
if b==-1:
    term2=" - x"
elif b<0:
    term2=" - " + str(abs(b)) + "x"
elif b==0:
    term2=""
elif b==1:
    term2="x"
elif b>0:
    term2=str(b) + "x"
else:
    term2=''
#checks for c
if c<0:
    term3=" - " + str(abs(c))
elif c==0:
    term3=""
elif c>0:
    term3=" + " +str(c)

print(f'The quadratic equation is {term1+term2+term3} = 0')