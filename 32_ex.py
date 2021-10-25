# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to get the least common multiple (LCM) of two positive integers.
# # Exercise 33

first_number = int(input("Input first number: "))
second_number = int(input("\nInput second number: "))


def finding_lcm(numb_1, numb_2):
    if numb_1 > numb_2:
        growing_number = numb_1
    else:
        growing_number = numb_2

    while True:
        if growing_number % numb_1 == 0 and growing_number % numb_2 == 0:
            lcm = growing_number
            break
        growing_number += 1
    return lcm


print("The LCM is: ", finding_lcm(first_number, second_number))
