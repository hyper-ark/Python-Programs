#Assume a machine during its initial testing phase produces 10 gadgets a day. After 10 days of testing (starting on day 11), it begins to ramp up, producing 1 more gadget per day (11 gadgets on day 11, 12 on day 12, etc). On day 50 it reaches full speed, where it continues to run until on day 101 it stops producing gadgets. Write a program named how_many_gadgets.py that reads in a day (as a number) from the keyboard and reports the total number of gadgets produced from the initial testing phase up to and including the day entered.

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: Lab 4.18 How many gadgets
# Date: 14 September 2023

days = int(input("Please enter a positive value for day: "))

#calculations
if days<0:
    print("You entered an invalid number!")
elif days <= 10:
    gadgets = 10*days
    print(f"The sum total number of gadgets produced on day {days} is {gadgets}")
elif days <= 50:
        gadgets = 100 + 0.5*(10+days)*(days-10) + (0.5*(days-10))
        print(f"The sum total number of gadgets produced on day {days} is {gadgets:.0f}")
elif days <= 100:
    gadgets = 1320 + ((days-50)*50)
    print(f"The sum total number of gadgets produced on day {days} is {gadgets}")
else:
    print(f"The sum total number of gadgets produced on day {days} is {3820}")
