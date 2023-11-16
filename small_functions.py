# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: Lab 9.16
# Date: 27 10 2023

from math import *

def parta (s_radius, h_radius):
    
    h = s_radius - sqrt(s_radius**2 - h_radius**2)
    sphere_volume = (4/3) * pi * (s_radius**3)
    cylinder_volume = pi * (h_radius**2) * (2*s_radius - 2*h)
    caps_volume = (pi/3) * (h**2) * (3*s_radius - h)
    
    return sphere_volume - cylinder_volume - 2*caps_volume       #returning difference in volumes

def partb (n):
    
    odd_list = list(range(1,n,2))
    for a in range(len(odd_list)):
        
        for b in range(len(odd_list)-1,-1,-1):
            
            if sum(odd_list[a:b+1]) == n:
                
                return odd_list[a:b+1]
                #returning sublist of required numbers that add to n
            
    return False
            
def partc (c, name, company, email):
    
    if len(name) > len(company) and len(name) > len(email):
        width = len(name) + 6
    elif len(company) > len(name) and len(company) > len(email):
        width  = len(company) + 6
    elif len(email) > len(name) and len(email) > len(company):
        width = len(email) + 6
    
    output = f'{c*width}\n{c}{name.center(width-2)}{c}\n{c}{company.center(width-2)}{c}\n{c}{email.center(width-2)}{c}\n{c*width}'
    return output     #returning formatted output as one string

def partd (num_list):
    
    num_list.sort()
    minimum = num_list[0]
    maximum = num_list[-1]
    if len(num_list) % 2 == 1:
        median = num_list[len(num_list) // 2]
    else:
        median = (num_list[len(num_list)//2] + num_list[len(num_list)//2 - 1]) / 2
        
    return minimum, median, maximum   #returning values

def parte (time_list, dist_list):
    
    vel_list = []
    for position in range(len(time_list) - 1):
        
        vel_list.append((dist_list[position + 1] - dist_list[position]) / (time_list[position + 1] - time_list[position]))  
    
    return vel_list     #returning calculated velocities between times

def partf (num_list):

    for num1 in num_list:
        
        for num2 in num_list:
            
            if num1 + num2 == 2027:
                
                return num1 * num2        #returning product of nums
   
    return False