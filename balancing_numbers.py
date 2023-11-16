# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: Lab 6.16 Balancing numbers
# Date: 29 September 2023

n = int(input("Enter a value for n: "))
sum1 = 0
count = 0
sum2 = 0

#left sum
while count != n:
    sum1 += count
    count += 1
    
count =  0

#right sum
while sum2 < sum1:
    sum2 += (n + 1 + count)
    count += 1
    
#print result
if sum1 == sum2:
    print(f"{n} is a balancing number with r={count}")
else:
    print(f"{n} is not a balancing number")