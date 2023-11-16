# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names: Yuqing Cao
# Pooja Marella
# Arya Kumar
# Nicolaus Reali
# Section:      514
# Assignment:   passport checker
# Date:         7/11/2023

#open files
inp=input("Enter the name of the file: ")
passports=open(inp,'r')
valid_passports=open("valid_passports.txt","w")

all_lines=passports.readlines()
string=''
count=0

for i in all_lines:
    string+=i

lis=string.split('\n\n')
for i in lis:
    if 'pid' in i and 'hgt' in i and 'cid' in i and 'iyr' in i and 'byr' in i and 'hcl' in i and 'eyr' in i:
        valid_passports.write(i+'\n\n')
        count+=1
print(f'There are {count} valid passports')

#close files
passports.close()
valid_passports.close()