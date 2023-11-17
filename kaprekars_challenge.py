#Modify your program from Activity 4 to compute the sum of the number of iterations required to reach 6174 (or 0000) using Kaprekar’s routine for all four-digit numbers, from 0000 to 9999. Name your file kaprekars_challenge.py.

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: Lab 7.29 Kaprekar's constant challenge
# Date: 4 October 2023

#funtions for rewriting number
def ascending (s):
    s = list(s)
    s.sort();
    s = "".join(s)
    return int(s)

def descending (s):
    s = list(s)
    s.sort();
    s.reverse();
    s = "".join(s)
    return int(s)

starter_num = 0
iterations = 0
while starter_num != 10000:
    current_num = str(starter_num)
    
    #iterations loop
    while current_num != "6174":
        
        if current_num == "0":
            break
        
        if len(current_num) == 3:
            current_num = "0" + current_num
        elif len(current_num) == 2:
            current_num = "00" + current_num
        elif len(current_num) == 1:
            current_num = "000" + current_num
        
        num1 = ascending(current_num)
        num2 = descending(current_num)
        
        if num1 > num2:
            current_num = str(num1 - num2)
        else:
            current_num = str(num2 - num1)
            
        iterations += 1
        
    starter_num += 1

print(f"Kaprekar's routine takes {iterations} total iterations for all four-digit numbers")
