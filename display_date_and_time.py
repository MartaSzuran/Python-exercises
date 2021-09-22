# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Exercise 3

# import modules
import datetime

now = datetime.datetime.now()
print(now)
today = datetime.datetime.today()
print(today)
print(now.strftime("%d - %m - %Y %H:%M:%S"))
print(now.strftime("%d-%m-%y   %H:%M:%S"))
print(now.strftime("Date: %d-%m-%y\nTime: %H:%M:%S"))
