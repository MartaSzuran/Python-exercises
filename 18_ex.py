# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to calculate the sum of three given numbers,
# # if the values are equal then return three times of their sum.
# # Exercise 18

numbers = []
for i in range(3):
    given_number = int(input("Give me number: \n"))
    numbers.append(given_number)


def counting_sum(numbers_list):
    counter = 0
    for number in numbers_list:
        counter += int(number)
    return counter


numbers_sum = counting_sum(numbers)

if numbers[0] == numbers[1] == numbers[2]:
    print("Three time of sum of numbers: ", numbers[0], ",", numbers[1], ",", numbers[2], "is: ", 3*numbers_sum)
else:
    print("Sum of numbers: ", numbers[0], ",", numbers[1], ",", numbers[2], "is: ", numbers_sum)
