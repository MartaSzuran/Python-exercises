# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to print out a set containing all the colors from color_list_1
# # which are not present in color_list_2.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}
# # Exercise 29

# set data type:
# - cannot be changed after creating
# - we can add new thing into set
# - it could be set with different data types
# - creating set with : set(())
# - creating set with : set_1 = {}
color_list_1 = {"White", "Black", "Red"}
color_list_2 = set(("Red", "Green"))


def checking_set_items(set_1, set_2):
    set_with_items_not_in_set_2 = set(())
    equal = 0
    for i in set_1:
        for y in set_2:
            if i == y:
                equal += 1
        if equal == 0:
            set_with_items_not_in_set_2.add(i)
        equal = 0
    return set_with_items_not_in_set_2


print(checking_set_items(color_list_1, color_list_2))

# we can also use function difference() (from solution)
print("\nDifference of color_list_1 and color_list_2:")
print(color_list_1.difference(color_list_2))
print("\nDifference of color_list_2 and color_list_1:")
print(color_list_2.difference(color_list_1))
