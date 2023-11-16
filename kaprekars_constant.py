# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: Lab 7.28 Kaprekar's constant
# Date: 4 October 2023

#funtions for rewriting number
def ascending (s):
    s = list(s)
    s.sort();
    s = "".join(s)
    return s

def descending (s):
    s = list(s)
    s.sort();
    s.reverse();
    s = "".join(s)
    return s

#inputs and initialization
user_input = input("Enter a four-digit integer: ")
current_num = user_input
iterations = 0
output = user_input

#iterations loop
while current_num != "6174":
    
    if len(current_num) == 3:
        current_num = "0" + current_num
    elif len(current_num) == 2:
        current_num = "00" + current_num
    elif len(current_num) == 1:
        current_num = "000" + current_num
    
    num1 = ascending(current_num)
    num2 = descending(current_num)
    
    if int(num1) > int(num2):
        current_num = str(int(num1)-int(num2))
    else:
        current_num = str(int(num2)-int(num1))
        
    iterations += 1
    output += " > " + current_num
    
    if current_num == "6174" or current_num == "0":
        print(output)
        print(f"{user_input} reaches {current_num} via Kaprekar's routine in {iterations} iterations")
        break
    
    
    
    
    