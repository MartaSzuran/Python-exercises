# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
# # Exercise 40

import math

print("Give me dimensions of to points: ")
dimension_x_1 = int(input("X of the first dimensions: "))
dimension_y_1 = int(input("Y of the first dimensions: "))
dimension_x_2 = int(input("X of the second dimensions: "))
dimension_y_2 = int(input("Y of the second dimensions: "))


def distance(x_1, y_1, x_2, y_2):
    # using math function sqrt()
    # returns floating point number like 5.0
    # formula  = sqrt(((x1 - x2)**2)+((y1-y2)**2))
    dis = math.sqrt(((x_1 - x_2)**2)+((y_1 - y_2)**2))
    return dis


print("The distance is: ", round(distance(dimension_x_1, dimension_y_1, dimension_x_2, dimension_y_2), 2))
