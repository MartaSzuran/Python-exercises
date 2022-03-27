# # https://www.w3resource.com/python-exercises/list/
# # Write a Python program to clone or copy a list.

sample_list_1 = [1, 5, 6, 7, 3, 3, 7, 3]


def copy_list(exmp_list):
    list_copy = exmp_list.copy()
    return list_copy


print("Basic list: ", sample_list_1, "\ncopy: ", copy_list(sample_list_1))

