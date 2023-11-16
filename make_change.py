# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Yuqing Cao
# Pooja Marella
# Arya Kumar
# Nicolaus Reali
# Section: 514
# Assignment: make_change – team
# Date: 9/8/2023

#taking inputs
paid=float(input("How much did you pay? "))
cost=float(input("How much did it cost? "))
change1=paid-cost

def change(c):
    print(f"You received ${change1:.2f} in change. That is...")
    c=c*100
    if c>25:
        q=int(c//25)
        c=c%25
        if (q>0):
            if (q>1):
                print(q, "quarters")
            else:
                print(q, "quarter")
    
    if c>10:
        d=int(c//10)
        c=c%10
        if (d>0):
            if (d>1):
                print(d, "dimes")
            else:
                print(d, "dime")
    
    if c>5:
        n=int(c//5)
        c=c%5
        if (n>0):
            if (n>1):
                print(n, "nickels")
            else:
                print(n, "nickel")
    
    if c>0:
        p=round(c)
        if (p>0):
            if (p>1):
                print(p, "pennies")
            else:
                print(p, "penny")

change(change1)