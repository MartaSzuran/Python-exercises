# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to display the first and last colors from the following list
# # color_list = ["Red","Green","White" ,"Black"]
# # Exercise 8

color_list = ["Red", "Green", "White", "Black"]
list_length = len(color_list)
print("The first color is:", color_list[0], "and the last one is:", color_list[list_length-1])

# another solution
print("%s %s" % (color_list[0], color_list[-1]))
