# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to solve (x + y) * (x + y)
# # Exercise 38

numb_1 = int(input("Give me first number: "))
numb_2 = int(input("Give me second number: "))


def calculation(number_1, number_2):
    solution = (number_1 + number_2)*(number_1 + number_2)    # (number_1 + number_2)^2
    return solution


print(calculation(numb_1, numb_2))
