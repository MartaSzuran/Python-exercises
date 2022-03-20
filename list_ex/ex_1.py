# https://www.w3resource.com/python-exercises/list/
# Write a Python program to sum all the items in a list.

sample_list = [1, 4, 623, 't']


def sum_list_elements(list_example):
    """Function that return sum of all list elements."""
    el_sum = 0
    for element in list_example:
        if element is int:
            el_sum += element
        else:
            print("Some of elements in the list are not a number!")
            break

    return el_sum


sum_of_list_elements = (sum_list_elements(sample_list))
if sum_of_list_elements != 0:
    print(sum_of_list_elements)
