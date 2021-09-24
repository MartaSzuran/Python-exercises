# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program which accepts a sequence of comma-separated numbers from user
# # and generate a list and a tuple with those numbers
# # Exercise 6

# my solution / but it splits also 23 to [2,3]
numbers = input("Give me number separated using commas: ")
numbers_list = []
for number in numbers:
    if number != " " and number != ",":
        number = int(number)
        numbers_list.append(number)

# we cannot add anything to tuple because it is immutable
# so we need to define it with the ending result
numbers_tuple = tuple(numbers_list)
print(numbers)
print(numbers_tuple)
print(numbers_list)

# page solution

values = input("Input some comma seprated numbers : ")
#  str.split(sep=None, maxsplit=-1)
# Return a list of the words in the string, using sep as the delimiter string.
# If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements).
# If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).
# If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings
# (for example, '1,,2'.split(',') returns ['1', '', '2']).
# The sep argument may consist of multiple characters (for example, '1<>2<>3'.split('<>') returns ['1', '2', '3']).
# Splitting an empty string with a specified separator returns [''].

list = values.split(",")
tuple = tuple(list)
print('List : ', list)
print('Tuple : ', tuple)
