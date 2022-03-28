# # https://www.w3resource.com/python-exercises/list/
# #  Write a Python function that takes two lists and returns True if they have at least one common member.

sample_list_1 = [2, 5, 6, 7]
sample_list_2 = [1, 3, 5, 7]
sample_list_3 = [4, 0, 8, 9]


def find_common_member(list_1, list_2):
    common_member = 0
    for member in list_1:
        for element in list_2:
            if member == element:
                common_member += 1

    if common_member > 0:
        return True
    else:
        return False


print(find_common_member(sample_list_1, sample_list_2))
print(find_common_member(sample_list_1, sample_list_3))
