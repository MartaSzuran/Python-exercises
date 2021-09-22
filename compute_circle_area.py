# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Exercise 4

# ask for radius input from user
# my solution
radius = float(input("Radius: "))
PI = 3.14
circle_area = PI*radius**2
circle_area_2 = PI * pow(radius, 2)

print("\nArea of the circle with radius:", radius, "is: ", round(circle_area,4))

input("For finish press Enter.")

# other solution
# from math import pi
# r = float(input("Input the radius of the circle : "))
# print("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
