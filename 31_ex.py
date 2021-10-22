# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to compute the greatest common divisor (GCD) of two positive integers.
# # Exercise 31

numb_1 = int(input("Input first number: "))
numb_2 = int(input("\nInput second number: "))


def finding_gcd(x, y):
    gcd = 1
    # if x % y = 0 y is the greatest common divisor
    if x % y == 0:
        gcd = y

    # if not I need to look for it
    # range function from y/2 to 0 step less by 1 (-1)
    for numb in range(int(y/2), 0, -1):
        if x % numb == 0 and y % numb == 0:
            gcd = numb
            break
    return gcd


print(finding_gcd(numb_1, numb_2))
