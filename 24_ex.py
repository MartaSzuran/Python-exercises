# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to test whether a passed letter is a vowel or not.
# # Exercise 24

letter = input("Give me the letter: ")
vowels = ["a", "e", "i", "o", "y"]
if letter in vowels:
    print("Letter is the vowel")
else:
    print("Letter is not the vowel")
