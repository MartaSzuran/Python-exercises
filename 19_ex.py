# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to get a new string from a given string where "Is" has been added to the front.
#  # If the given string already begins with "Is" then return the string unchanged.
# # Exercise 19

def get_string(sent):
    if sentence[:2] == "Is":
        print(sent)
    else:
        print("Is " + sent)


sentence = input("Give me a sentence:\n")
get_string(sentence)
