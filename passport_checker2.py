#Write a program named passport_checker2.py that takes as input from the user a filename, reads the file, counts the number of valid passports based on the rules below, then writes the valid passport scans to a new file named valid_passports2.txt. Format your program’s output and your new file using the same format as Part A.

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names: Yuqing Cao
# Pooja Marella
# Arya Kumar
# Nicolaus Reali
# Section:      514
# Assignment:   passport checker2
# Date:         7/11/2023

#open files
inp=input("Enter the name of the file: ")
passports=open(inp,'r')
valid_passports=open("valid_passports2.txt","w")

all_lines=passports.readlines()
string=''
count=0
validlist=[]

for i in all_lines:
    string+=i

lis=string.split('\n\n')
for i in lis:
    if 'pid' in i and 'hgt' in i and 'cid' in i and 'iyr' in i and 'byr' in i and 'hcl' in i and 'eyr' in i:
        validlist.append(i)

for passportwritten in validlist:
    tempList = passportwritten.split("\n")
    tempList2 = []
    tempList3 = []
    for j in tempList:
        tempList2.append(j.split(" "))
    for k in range(len(tempList2)):
        for l in range(len(tempList2[k])):
            tempList3.append(tempList2[k][l])
    isValid = True
    for i in tempList3:
        if i[0:3] == "pid":
            if len(i) - 4 != 9:
                isValid = False
                break
            else:
                continue
        if i[0:3] == "hgt":
            if i[-2:] == "cm":
                if 193 < int(i[4:-2]) or int(i[4:-2]) < 150:
                    isValid=False
                    break
            elif i[-2:] == "in":
                if 76 < int(i[4:-2]) or int(i[4:-2]) < 59:
                    isValid=False
                    break
            else:
                isValid=False
                break
        if i[0:3] == "cid":
            if int(i[4:])>999 or int(i[4:])<100:
                isValid=False
                break
        if i[0:3] == "iyr":
            if int(i[4:])>2023 or int(i[4:])<2013:
                isValid=False
                break
        if i[0:3] == "byr":
            if int(i[4:])>2007 or int(i[4:])<1920:
                isValid=False
                break
        if i[0:3] == "eyr":
            if int(i[4:])>2033 or int(i[4:])<2023:
                isValid=False
                break
        if i[0:3] == "hcl":
            if i[4] != "#":
                isValid=False
                break
            else:
                if len(i) - 5 != 6:
                    isValid=False
                    break
                else:
                    for x in i[5:]:
                        if x not in "0123456789abcdef":
                            isValid=False
                            break
    if isValid == True:
        count += 1
        valid_passports.write(passportwritten+'\n\n')
print(f'There are {count} valid passports')

#close files
passports.close()
valid_passports.close()
