# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to test whether a number is within 100 of 1000 or 2000.
# # Exercise 17

number = int(input("Give me number: "))

if number < 100:
    print("\n", number, "is less then 100.")
elif 100 <= number <= 1000:
    print("\n", number, "is between 100 and 1000.")
elif 1000 <= number <= 2000:
    print("\n", number, "is between 1000 and 2000.")
else:
    print("\n", number, "is greater then 2000.")

