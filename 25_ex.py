# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to check whether a specified value is contained in a group of values.
# # Example
# # Test Data :
# # 3 -> [1, 5, 8, 3] : True
# # -1 -> [1, 5, 8, 3] : False
# # Exercise 25

list_of_numbers = [1, 5, 8, 3]


def test(numb, list_of_numb):
    if numb in list_of_numb:
        print("Value", numb, "is in the list.")
    else:
        print("Value", numb, "is not in the list.")


number = int(input("Give me number: "))
test(number, list_of_numbers)
