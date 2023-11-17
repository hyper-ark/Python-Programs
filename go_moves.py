#The purpose of this activity is to get you used to using lists of lists, in a 2-D matrix-like format. Your team will create a program that sets up a small Go board and lets users place stones.

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."

# Name: Yuqing Cao
# Arya Kumar
# Pooja Marella
# Nicolaus Reali
# Section: 514
# Assignment: LAB: Topic 7 (team)
# Date: 30 September 2023

#board generation
lis=[['.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.'],['.','.','.','.','.','.','.','.','.']]

#function to print board
def table():
    for i in range(len(lis)):           #prints rows
        for a in range(len(lis[i])):    #prints columns
            if a%9==0:
                print()
            print(lis[i][a], end=" ")

#first inputs and output            
table()
row=int(input('\nPlease input the position of your next move for rows: '))
column=int(input('Please input the position of your next move for columns: '))
stop='GO'
count=0

#game algorithm
while stop!='STOP':
    stop=input("Type 'STOP' to stop; type 'GO' to continue: ")
    if stop=='STOP':
        table()
        break
    elif stop=='GO':
        if row > 8 or row < 0 or column > 8 or column < 0:
            print("The position is out of bounds. Please try again.")
        elif lis[row][column] == 'o' or lis[row][column] == 'O':
            print("A stone already exists. Please try again.")
        else:
            count+=1
            if count%2==1:
                lis[row][column]='o'
            else:
                lis[row][column]='O'
    table()
    row=int(input('\nPlease input the position of your next move for rows: '))
    column=int(input('Please input the position of your next move for columns: '))

