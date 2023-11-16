# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Arya Kumar
# Section: 514
# Assignment: Lab 2.1
# Date: 1 September 2023

#two given positions
t1 = 12
t2 = 85
x1 = 8
x2 = -5
y1 = 6
y2 = 30
z1 = 7
z2 = 9

#x y z slope calculation
slope_x = (x2 - x1) / (t2 - t1)
slope_y = (y2 - y1) / (t2 - t1)
slope_z = (z2 - z1) / (t2 - t1)

t = 30.0
x_1 = (slope_x) * (t - t1) + x1
y_1 = (slope_y) * (t - t1) + y1
z_1 = (slope_z) * (t - t1) + z1
print("At time {} seconds:".format(t))
print("x1 = {} m".format(x_1))
print("y1 = {} m".format(y_1))
print("z1 = {} m".format(z_1))
print("-----------------------")

t += (30 / 4)
x_2 = (slope_x) * (t - t1) + x1
y_2 = (slope_y) * (t - t1) + y1
z_2 = (slope_z) * (t - t1) + z1
print("At time {} seconds:".format(t))
print("x2 = {} m".format(x_2))
print("y2 = {} m".format(y_2))
print("z2 = {} m".format(z_2))
print("-----------------------")

t += (30 / 4)
x_3 = (slope_x) * (t - t1) + x1
y_3 = (slope_y) * (t - t1) + y1
z_3 = (slope_z) * (t - t1) + z1
print("At time {} seconds:".format(t))
print("x3 = {} m".format(x_3))
print("y3 = {} m".format(y_3))
print("z3 = {} m".format(z_3))
print("-----------------------")

t += (30 / 4)
x_4 = (slope_x) * (t - t1) + x1
y_4 = (slope_y) * (t - t1) + y1
z_4 = (slope_z) * (t - t1) + z1
print("At time {} seconds:".format(t))
print("x4 = {} m".format(x_4))
print("y4 = {} m".format(y_4))
print("z4 = {} m".format(z_4))
print("-----------------------")

t += (30 / 4)
x_5 = (slope_x) * (t - t1) + x1
y_5 = (slope_y) * (t - t1) + y1
z_5 = (slope_z) * (t - t1) + z1
print("At time {} seconds:".format(t))
print("x5 = {} m".format(x_5))
print("y5 = {} m".format(y_5))
print("z5 = {} m".format(z_5))