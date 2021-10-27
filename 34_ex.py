# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program that will return true if the two given integer values are equal
# # or their sum or difference is 5.
# # Exercise 34

number_1 = int(input("Input first number: "))
number_2 = int(input("\nInput second number: "))


def operation(numb_1, numb_2):
    sum_of_two_numbers = numb_1 + numb_2
    difference_of_two_numbers = numb_1 - numb_2
    if sum_of_two_numbers == 5:
        return True
    elif difference_of_two_numbers == 5 or difference_of_two_numbers == -5:
        return True
    elif numb_1 == numb_2:
        return True
    else:
        return False


print(operation(number_1, number_2))
