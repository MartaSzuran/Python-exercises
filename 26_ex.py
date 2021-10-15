# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to create a histogram from a given list of integers.
# # Exercise 26

list_of_integers = [2, 4, 6, 1, 5]


def histogram(numb_list):
    for numb in numb_list:
        print("#" * numb)


histogram(list_of_integers)
