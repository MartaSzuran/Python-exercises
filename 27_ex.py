# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to concatenate all elements in a list into a string and return it.
# # Exercise 27


list_of_elements = []

print("Give me 5 elements.")
for i in range(5):
    element = input("Element: ")
    list_of_elements.append(element)


def chain_list_elements(list_of_elem):
    new_string = ""
    for list_element in list_of_elem:
        new_string += list_element

    return new_string


chained_string = chain_list_elements(list_of_elements)
print(chained_string)
