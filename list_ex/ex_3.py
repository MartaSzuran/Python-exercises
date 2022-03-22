# https://www.w3resource.com/python-exercises/list/
# Write a Python program to get the largest number from a list.

sample_list = [1, 4, 623, 54]


def largest_number(list_1):
    the_biggest_number = list_1[0]
    for number in list_1:
        if number > the_biggest_number:
            the_biggest_number = number

    return the_biggest_number


print("The largest number in the list is: ", largest_number(sample_list))
