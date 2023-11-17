#Write a program named pixel_painter.py that takes as input a filename and a character, converts the contents of the file to pixel art, and writes the art to a new file of the same name but with the .txt extension. The first value in a line always corresponds to the number of light pixels.

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: 11.12 LAB
# Date: 9 11 2023

file_name = input("Enter the filename: ")
new_file_name = file_name[:file_name.index(".")] + ".txt"
char = input("Enter a character: ")
new_file = open(new_file_name, "w")

#iterating through data values in file
with open(file_name, "r") as file:
    
    for line in file:
        
        pixel = 0
        nums = line.strip()
        nums = nums.split(",")
        
        for num in nums:
        
            if pixel%2 == 0:
                new_file.write(int(num) * " ")
            else:
                new_file.write(int(num) * char)
            pixel += 1
            
        new_file.write("\n")

new_file.close()
print(f"{new_file_name} created!")
