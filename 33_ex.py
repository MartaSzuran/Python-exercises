# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
# # Exercise 33

print("Input 3 integers: ")
numbers = []
for i in range(3):
    number = int(input("Number:"))
    numbers.append(number)


def operation(list_of_numbers):
    if list_of_numbers[0] == list_of_numbers[1]:
        sum_of_list_numbers = 0
        return sum_of_list_numbers
    elif list_of_numbers[1] == list_of_numbers[2]:
        sum_of_list_numbers = 0
        return sum_of_list_numbers
    elif list_of_numbers[0] == list_of_numbers[2]:
        sum_of_list_numbers = 0
        return sum_of_list_numbers
    else:
        sum_of_list_numbers = list_of_numbers[0] + list_of_numbers[1] + list_of_numbers[2]
    return sum_of_list_numbers


print("Sum of number: ", operation(numbers))
