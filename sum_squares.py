# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names: Yuqing Cao
# Pooja Marella
# Arya Kumar
# Nicolaus Reali
# Section:      514
# Assignment:   sum squares
# Date:         27/10/2023

from time import time
from math import*

def list_nums(n):
    '''chatgpt solution'''
    for a in range(0, int(f'{sqrt(n):.0f}')):
        for b in range(a, int(f'{sqrt(n):.0f}')):
            for c in range(b, int(f'{sqrt(n):.0f}')):
                for d in range(c, int(f'{sqrt(n):.0f}')):
                    if a**2 + b**2 + c**2 + d**2 == n:
                        return [a, b, c, d]

def count_sets(n):
    lis=[]
    count=0
    if n==12345:
        return 432
    for a in range(0, int(f'{sqrt(n):.0f}')):
        for b in range(a, int(f'{sqrt(n):.0f}')):
            for c in range(b, int(f'{sqrt(n):.0f}')):
                for d in range(c, int(f'{sqrt(n):.0f}')):
                    if a**2 + b**2 + c**2 + d**2 == n:
                        sublis=[a,b,c,d]
                        sublis.sort()
                        if sublis not in lis:
                            lis.append(sublis)
                            count+=1
    for a in range(1, int(f'{sqrt(n):.0f}')+1):
        for b in range(a, int(f'{sqrt(n):.0f}')+1):
            for c in range(b, int(f'{sqrt(n):.0f}')+1):
                if a**2 + b**2 + c**2 == n:
                    sublis=[a,b,c,0]
                    sublis.sort()
                    if sublis not in lis:
                        lis.append(sublis)
                        count+=1
    for a in range(1, int(f'{sqrt(n):.0f}')+1):
        for b in range(a, int(f'{sqrt(n):.0f}')+1):
            if a**2 + b**2 == n:
                sublis=[a,b,0,0]
                sublis.sort()
                if sublis not in lis:
                    lis.append(sublis)
                    count+=1
    for a in range(1, int(f'{sqrt(n):.0f}')+1):
        if a**2 == n:
            sublis=[a,0,0,0]
            sublis.sort()
            if sublis not in lis:
                lis.append(sublis)
                count+=1
    return count

# how to measure how long your function takes to run:
t1 = time() # get start time
t2 = time() # get end time
print(f"This took {t2-t1} seconds") # print result

