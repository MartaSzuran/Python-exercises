# # https://www.w3resource.com/python-exercises/list/
# # Write a Python program to get the largest number from a list.

sample_list = [10, 4, 623, 54]


def searching_the_smallest_numb(example_list):
    the_smallest_number = example_list[0]
    for number in example_list:
        if number < the_smallest_number:
            the_smallest_number = number

    return the_smallest_number


print("The smallest number from the list is: ", searching_the_smallest_numb(sample_list))
