# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to get a string which is n (non-negative integer) copies of a given string.
# # Exercise 20

text = input("Give me a string of characters: ")

number = int(input("\nGive me number of copies you would like to get: "))


def copy_string(txt, n):
    if n > 0:
        print((txt + "\n")*n)
    else:
        print(txt)


copy_string(text, number)
