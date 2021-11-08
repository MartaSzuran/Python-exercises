# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to check whether a file exists.
# # Exercise 41

import os.path

# first solution
print(os.path.isfile("42_ex.py"))
print(os.path.isfile("40_ex.py"))

# second solution
print(os.path.exists("42_ex.py"))
print(os.path.exists("40_ex.py"))

# third solution
my_file = open("40_ex.py")
try:
    my_file.close()
    print("File found.")
except FileNotFoundError:
    print("File not found.")
