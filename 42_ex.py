# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
# # Exercise 42

# For 32 bit it will return 32 and for 64 bit it will return 64
import struct
print(struct.calcsize("P") * 8)


# tip of the day
import collections

A = collections.Counter([1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7])
print(A)
# show the most common number in this case 3, and after "," how many times it appears in that example 4
print(A.most_common(1))
print(A.most_common(3))
