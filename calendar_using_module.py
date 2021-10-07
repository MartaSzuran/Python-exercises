# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to print the calendar of a given month and year.
# # Note : Use 'calendar' module.
# # Exercise 12

import calendar

year = int(input("Input year: "))
month = int(input("\nInput month: "))

print(calendar.month(year, month))

# my mistake
# More than likely you have a local document calendar.py
# that is imported rather than the module in the standard library.
# Discover where by printing the module:

# import calendar
# print(calendar)
