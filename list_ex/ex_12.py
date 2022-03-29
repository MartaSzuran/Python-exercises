# # https://www.w3resource.com/python-exercises/list/
# #  Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

list_1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']


def remove_elements(sample_list):
    sample_list.pop(0)
    sample_list.pop(4)
    sample_list.pop(-1)
    return sample_list


print("New list: ", remove_elements(list_1))
