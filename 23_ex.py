# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# # Return the n copies of the whole string if the length is less than 2
# # Exercise 23

text = input("Give me string: ")
number_of_copies = int(input("\nGive me number of copies: "))

list_of_characters = []

for character in text:
    if character != " ":
        list_of_characters.append(character)

# print(list_of_characters)

if len(text) <= 2:
    print(text)
else:
    first_two_characters = list_of_characters[0] + list_of_characters[1]
    # print(first_two_characters)
    print(number_of_copies*first_two_characters)
