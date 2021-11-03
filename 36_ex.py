# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to add two objects if both objects are an integer type
# # Exercise 36

# The isinstance() function returns True if the specified object is of the specified type, otherwise False.
# If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.
# syntax  =  isinstance(object, type)

# Check if "Hello" is one of the types described in the type parameter:
# x = isinstance("Hello", (float, int, str, list, dict, tuple))

def check_if_is_a_number(obj_1, obj_2):
    if isinstance(obj_1, int) and isinstance(obj_2, int):
        return obj_1 + obj_2
    else:
        return "\nInputs must be integers."


print(check_if_is_a_number('a', 'b'))
print(check_if_is_a_number(3, '5'))
print(check_if_is_a_number(10, 23))
