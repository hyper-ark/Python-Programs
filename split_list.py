# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: Lab 7.27 Split list
# Date: 4 October 2023

def list_sum (l):
    sum = 0
    for i in l:
        sum+=i
    return sum

user_input = input("Enter numbers: ").split(" ")
for num in user_input:
    user_input[user_input.index(num)] = int(num)
split_val = 1

#splitting lists
while split_val <= len(user_input):
    left_list = user_input[0:split_val]
    right_list = user_input[split_val:]
    if list_sum(left_list) == list_sum(right_list):
        print(f"Left: {left_list}")
        print(f"Right: {right_list}")
        print(f"Both sum to {list_sum(left_list)}")
        break
    if split_val == len(user_input):
        print("Cannot split evenly")
        break
    split_val += 1