# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to calculate number of days between two dates.
# # Sample dates : (2014, 7, 2), (2014, 7, 11)
# # Expected output : 9 days
# # Exercise 14

from datetime import date

date_1 = date(2013, 9, 5)
date_2 = date(2015, 8, 30)
number_of_days = date_2 - date_1

# if i print just number_of_days it will appear with hour
print("Number of days between dates", date_1, date_2, "is: \n", number_of_days.days)
