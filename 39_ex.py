# # Python exercise
# # source - https://www.w3resource.com/python-exercises/python-basic-exercises.php
# # Python Basic (Part -I) - Exercises, Practice, Solution
# # Write a Python program to compute the future value of a specified principal amount,
# # rate of interest, and a number of years.
# # Exercise 39

amount = int(input("Input amount of credit: "))
interests = float(input("Input interests rate: "))
years = int(input("Input how many years: "))


def count_future_value(p, r, t):

    # The formula for future value with compound interest is FV = P(1 + r/n)^nt.
    # FV = the future value;
    # P = the principal;
    # r = the annual interest rate expressed as a decimal;
    # n = the number of times interest is paid each year;
    # t = time in years.
    fv = p*((1+(0.01*r)) ** t)
    return fv


future_value = count_future_value(amount, years, interests)
print("Future value: ", round(future_value, 2))
