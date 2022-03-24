# # https://www.w3resource.com/python-exercises/list/
# # Write a Python program to get a list, sorted in increasing order by the last element in each tuple
# # from a given list of non-empty tuples.

# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# solution for sorting tuples inside increasing
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


def sort_list_of_tuples(list_example):
    sorted_list = []
    for tuple_element in list_example:
        # change tuple element into list to sort it and than convert into tuple again
        list_element = list(tuple_element)
        list_element.sort()
        tuple_element = tuple(list_element)
        sorted_list.append(tuple_element)

    return sorted_list


print("List with sorted tuples: ", sort_list_of_tuples(sample_list))


# solution from the web

# def last take last value from the tuple
def last(n):
    return n[0]
# function sorted take tuples from list of tuples
# - iterate through this list
# - take key from last function (in this case last element from the tuple)
# return list of sorted tuples
def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last(sample_list))
