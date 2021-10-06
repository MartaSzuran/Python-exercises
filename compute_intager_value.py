# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn
# # Exercise 10


# my solution
number_1 = input("Give me number: ")

# computing number n + nn + nnn
number_2 = number_1 + number_1
number_3 = number_1 + number_1 + number_1
compute_number = int(number_1) + int(number_2) + int(number_3)
print("Result: %i" % compute_number)

# page solution
a = int(input("Input an integer : "))
n1 = int("%s" % a)
n2 = int("%s%s" % (a, a))
n3 = int("%s%s%s" % (a, a, a))
print(n1+n2+n3)
