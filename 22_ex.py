# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to count how many times the number 4 is in a given list.
# # Exercise 22

list_of_numbers = []
print("Input 5 numbers.")
list_len = 5
for i in range(5):
    number = int(input("Number: "))
    list_of_numbers.append(number)


print(list_of_numbers)
count = 0
for number in list_of_numbers:
    if number == 4:
        count += 1

print("In given list there are/is", count, "four(s).")
