# # https://www.w3resource.com/python-exercises/list/
# #  Write a Python program to remove duplicates from a list.

sample_list_1 = [1, 5, 6, 7, 3, 3, 7, 3]
sample_list_2 = ["abc", "abc", "cds", "fbe"]


def remove_duplicates(list_ex):
    # create set - Sets cannot have two items with the same value.
    dupl_set = set()
    for element in list_ex:
        dupl_set.add(element)

    return list(dupl_set)


print("List without duplicates: ", remove_duplicates(sample_list_1))
print("List without duplicates: ", remove_duplicates(sample_list_2))
