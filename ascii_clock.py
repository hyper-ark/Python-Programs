#Write a program to take as input from the user a time and display that time using ASCII art. Draw each digit three (3) characters wide and five (5) characters tall, and the colon one (1) character wide. Also take as input from the user the clock type as well as a preferred character. Draw one space between the digits, colon, and letters. You do NOT need a leading zero or blank space for times earlier than noon.

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Yuqing Cao
# Pooja Marella
# Arya Kumar
# Nicolaus Reali
# Section: 514
# Assignment: ascii_clock – team
# Date: 13/10/2023

#Arya
#get user input
t=input("Enter the time: ")
c_type=input("Choose the clock type (12 or 24): ")
c=input("Enter your preferred character: ")
am=True
#check if input is valid
while c not in ' abcdeghkmnopqrsuvwxyz@$&*=':
    c=input("Character not permitted! Try again: ")
    
#turn t into list with two items
t_lis=t.split(":")

#turn each into integer
for i in range(len(t_lis)):
    t_lis[i]=int(t_lis[i])

#deciding if the 12 hour time will be am or pm and changes 24 hr time to 12hr time
if c_type=='12':
    if t_lis[0] > 12:
        t_lis[0]-=12
        am = False
    if t_lis[0] == 0:
        t_lis[0] = 12

#Nicolaus
#adding a zero to minutes if it's less than 2 digits
if t_lis[1]<10:
    t_lis[1]='0'+str(t_lis[1])

#converting items in t_lis into string
for i in range(len(t_lis)):
    t_lis[i]=str(t_lis[i])

#making the time into one string

t = ':'.join(t_lis)

#Yuqing
first_n=0
second_n=0
third_n=0
fourth_n=0

#obtain each number in time separately
if t[2]==':':
    first_n=int(t[0])
    second_n=int(t[1])
    third_n=int(t[3])
    fourth_n=int(t[4])
elif t[1]==':':
    first_n=int(t[0])
    second_n=int(t[2])
    third_n=int(t[3])
    fourth_n=''

#put each character into a list
lis_numbers=[
    #zero
    [c+c+c,c+' '+c,c+' '+c,c+' '+c,c+c+c],
    #one
    [' '+c+' ',c+c+' ',' '+c+' ',' '+c+' ',c+c+c],
    #two
    [c+c+c,' '+' '+c,c+c+c,c+' '+' ',c+c+c],
    #three
    [c+c+c,' '+' '+c,c+c+c,' '+' '+c,c+c+c],
    #four
    [c+' '+c,c+' '+c,c+c+c,' '+' '+c,' '+' '+c],
    #five
    [c+c+c,c+' '+' ',c+c+c,' '+' '+c,c+c+c],
    #six
    [c+c+c,c+' '+' ',c+c+c,c+' '+c,c+c+c],
    #seven
    [c+c+c,' '+' '+c,' '+' '+c,' '+' '+c,' '+' '+c],
    #eight
    [c+c+c,c+' '+c,c+c+c,c+' '+c,c+c+c],
    #nine
    [c+c+c,c+' '+c,c+c+c,' '+' '+c,c+c+c]
    ]

#Nicolaus
lis_n=[
    #zero
    ["000",'0 0','0 0','0 0','000'],
    #one
    [' 1 ','11 ',' 1 ',' 1 ','111'],
    #two
    ['222','  2','222','2  ','222'],
    #three
    ['333','  3','333','  3','333'],
    #four
    ['4 4','4 4','444','  4','  4'],
    #five
    ['555','5  ','555','  5','555'],
    #six
    ['666','6  ','666','6 6','666'],
    #seven
    ['777','  7','  7','  7','  7'],
    #eight
    ['888','8 8','888','8 8','888'],
    #nine
    ['999','9 9','999','  9','999']
    ]

lis_colon=[' ',':',' ',':',' ']
lis_a = [' A ','A A','AAA','A A','A A']
lis_p=['PPP','P P','PPP','P  ','P  ']
lis_m=['M   M','MM MM','M M M','M   M','M   M']

#Pooja
print()
if c!= "":
    for i in range(5):
        if c_type=='24':
            if fourth_n!='':
                print(lis_numbers[first_n][i],lis_numbers[second_n][i],lis_colon[i],lis_numbers[third_n][i],lis_numbers[fourth_n][i])
            else:
                print(lis_numbers[first_n][i],lis_colon[i],lis_numbers[second_n][i],lis_numbers[third_n][i])
        elif c_type=='12':
            if am == True: 
                if fourth_n!='':
                    print(lis_numbers[first_n][i],lis_numbers[second_n][i],lis_colon[i],lis_numbers[third_n][i],lis_numbers[fourth_n][i], lis_a[i],lis_m[i])
                else:
                    print(lis_numbers[first_n][i],lis_colon[i],lis_numbers[second_n][i],lis_numbers[third_n][i], lis_a[i],lis_m[i])
            elif am == False:
                if fourth_n!='':
                    print(lis_numbers[first_n][i],lis_numbers[second_n][i],lis_colon[i],lis_numbers[third_n][i],lis_numbers[fourth_n][i], lis_p[i],lis_m[i])
                else:
                    print(lis_numbers[first_n][i],lis_colon[i],lis_numbers[second_n][i],lis_numbers[third_n][i], lis_p[i],lis_m[i])
elif c=="":
    for i in range(5):
        if c_type=='24':
            if fourth_n!='':
                print(lis_n[first_n][i],lis_n[second_n][i],lis_colon[i],lis_n[third_n][i],lis_n[fourth_n][i])
            else:
                print(lis_n[first_n][i],lis_colon[i],lis_n[second_n][i],lis_n[third_n][i])
        elif c_type=='12':
            if am == True: 
                if fourth_n!='':
                    print(lis_n[first_n][i],lis_n[second_n][i],lis_colon[i],lis_n[third_n][i],lis_n[fourth_n][i], lis_a[i],lis_m[i])
                else:
                    print(lis_n[first_n][i],lis_colon[i],lis_n[second_n][i],lis_n[third_n][i], lis_a[i],lis_m[i])
            elif am == False:
                if fourth_n!='':
                    print(lis_n[first_n][i],lis_n[second_n][i],lis_colon[i],lis_n[third_n][i],lis_n[fourth_n][i], lis_p[i],lis_m[i])
                else:
                    print(lis_n[first_n][i],lis_colon[i],lis_n[second_n][i],lis_n[third_n][i], lis_p[i],lis_m[i])
                    
