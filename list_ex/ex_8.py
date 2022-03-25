# # https://www.w3resource.com/python-exercises/list/
# #   Write a Python program to check a list is empty or not.

import sys

sample_list_1 = [1, 5, 6, 7, 3, 3, 7, 3]
sample_list_2 = []


def is_empty(list_example):
    # method called **Truth Value Testing**.
    if not list_example:
        print("The ", list_example, " is empty.")
    else:
        print("The ", list_example, " is not empty.")


def is_empty_bool(list_example):
    # method using bool expression.
    if bool(list_example):
        print("The ", list_example, " is not empty.")
    else:
        print("The ", list_example, " is empty.")


def is_empty_len(list_example):
    # method using bool expression.
    if len(list_example):
        print("The ", list_example, " is not empty.")
    else:
        print("The ", list_example, " is empty.")


print(is_empty(sample_list_1))
print(is_empty(sample_list_2))

print(is_empty_bool(sample_list_1))
print(is_empty_bool(sample_list_2))

print(is_empty_len(sample_list_1))
print(is_empty_len(sample_list_2))
