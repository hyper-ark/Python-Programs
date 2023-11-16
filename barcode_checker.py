# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: 11.11 LAB
# Date: 9 11 2023

file_name = input("Enter the name of the file: ")
valid_barcodes = open("valid_barcodes.txt","w")
count = 0

#reading lines of barcodes
with open(file_name, "r") as file:
    
    for next_line in file:
        barcode = next_line.strip()
        
        first_group = 0
        for i in range(0,len(barcode)-1,2):
            first_group += int(barcode[i])
            
        second_group = 0
        for i in range(1,len(barcode)-1,2):
            second_group += int(barcode[i])
        
        second_group *= 3
        total = first_group + second_group
        total = str(total)
        
        if 10 - int(total[-1]) == int(barcode[-1]):
            count += 1
            valid_barcodes.write(next_line)
            
valid_barcodes.close()
print(f"There are {count} valid barcodes")