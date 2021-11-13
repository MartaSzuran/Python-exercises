# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to locate Python site-packages
# # Exercise 44

import site

# site.getsitepackages(): Return a list containing all global site-packages directories.
print(site.getsitepackages())


# tips of the day
# Named tuples structure
# (create tuple-like objects that have fields accessible by attribute lookup as well as being indexable and iterable):

import collections

Point = collections.namedtuple("Point", ["position_1", "position_2"])
# create object
Points = Point(position_1=10.0, position_2=20.0)
print(Points.position_1, Points.position_2)
