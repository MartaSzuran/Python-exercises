# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.
# # Exercise 33

number_1 = int(input("Input first number: "))
number_2 = int(input("\nInput second number: "))


def operation(numb_1, numb_2):
    sum_of_two_numbers = numb_1 + numb_2
    if 15 <= sum_of_two_numbers <= 20:
        sum_of_two_numbers = 20
    return sum_of_two_numbers


sum_of_given_numbers = operation(number_1, number_2)
print("\nSum is: ", sum_of_given_numbers)
