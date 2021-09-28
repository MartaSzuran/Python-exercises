# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to accept a filename from the user and print the extension of that
# # Exercise 7

# 1 solution
file_name = input("Give me file name: ")
dot_position = 0
for i in file_name:
    if i == ".":
        dot_position += 1
        break
    else:
        dot_position += 1

extension = file_name[dot_position:]
print("The extension is: ", extension)

# 2 solution
file_name = input("Give me file name: ")
extension = file_name.split(".")
# take the last element of extension list
# print(extension)
print("The extension is: ", extension[-1])
