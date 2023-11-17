#Download the file WeatherDataCLL.csv and write a program named weather_data.py that does the following

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: 11.13 LAB
# Date: 9 11 2023

file = open("WeatherDataCLL.csv","r")
data = list(file)
months = {"January":1,"February":2,"March":3,"April":4,"May":5,"June":6,"July":7,
          "August":8,"September":9,"October":10,"November":11,"December":12}
minimum = 200
maximum = 0
temp_sum = 0
temp_count = 0
humidity_sum = 0
humidity_count = 0
wind_sum = 0
wind_count = 0
precip_days = 0
days = 0

#finding max and min temperatures
for num in range(1,len(data)):
    line = data[num]
    line = line.strip()
    line = line.split(",")

    if line[-1] != "":
        if int(line[-1]) < minimum:
            minimum = int(line[-1])
    if line[-2] != "":
        if int(line[-2]) > maximum:
            maximum = int(line[-2])

#output max and min temperatures
print(f"10-year maximum temperature: {maximum} F")
print(f"10-year minimum temperature: {minimum} F")
print()

#month and year input
month = input("Please enter a month: ")
year = input("Please enter a year: ")
print()

#iterating and calculating values
for num in range(1,len(data)):
    line = data[num]
    line = line.strip()
    line = line.split(",")
    date = line[0]
    date = date.split("/")
    
    if int(date[0]) == months[month] and date[2] == year:
        days += 1

        if line[-6] != "":
            wind_sum += float(line[-6])
            wind_count += 1
        if line[-5] != "0":
            precip_days += 1
        if line[-4] != "":
            humidity_sum += int(line[-4])
            humidity_count += 1
        if line[-3] != "":
            temp_sum += int(line[-3])
            temp_count += 1
        if line[-1] != "":
            if int(line[-1]) < minimum:
                minimum = int(line[-1])
        if line[-2] != "":
            if int(line[-2]) > maximum:
                maximum = int(line[-2])

#output values
print(f"For {month} {year}: ")
print(f"Mean average daily temperature: {(temp_sum / temp_count):.01f} F")
print(f"Mean relative humidity: {(humidity_sum / humidity_count):.01f}%")
print(f"Mean daily wind speed: {(wind_sum / wind_count):.02f} mph")
print(f"Percentage of days with precipitation: {((precip_days / days) * 100):.01f}%")

file.close()
