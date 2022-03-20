# https://www.w3resource.com/python-exercises/list/
#  Write a Python program to multiply all the items in a list.

sample_list = [1, 4, 623, 54]


def multi_el_list(list_samp):
    result = 1
    for element in list_samp:
        result *= element

    return result


print("Multiplication result is: ", multi_el_list(sample_list))
