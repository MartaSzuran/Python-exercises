# # https://www.w3resource.com/python-exercises/list/
# # Write a Python program to count the number of strings where the string length is 2
# or more and the first and last character are same from a given list of strings
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2

sample_list = ['abc', 'xyz', 'aba', '1221']


def check_list(list_example):
    counter = 0
    for string in list_example:
        if len(string) > 2:
            first_letter = string[0]
            last_letter = string[-1]
            if first_letter == last_letter:
                counter += 1

    return counter


print("Number of strings where the string length is 2or more and the first and last character are same: ",
      check_list(sample_list))
