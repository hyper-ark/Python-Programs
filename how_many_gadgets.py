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
