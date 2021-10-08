# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to get the difference between a given number and 17,
# # if the number is greater than 17 return double the absolute difference
# # Exercise 16

base_number = 17
number = int(input("Give me any number: "))
difference = 0

if number > base_number:
    difference = (number - base_number)*2
    print("The double difference between", number, "and 17 is: ", difference)
else:
    difference = base_number - number
    print("The difference between", number, "and 17 is: ", difference)

# their solution
# def difference(n):
    # if n <= 17:
        # return 17 - n
    # else:
        # return (n - 17) * 2

# print(difference(22))
# print(difference(14))
