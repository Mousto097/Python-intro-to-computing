# Author: Mamadou Bah

import math


def pythagorean_pair(a, b):
    "Returns True if a and b are pythagorean pair and False otherwise"

    # Flag variable and is set to False at the begining
    result = False

    # Check if a and b are both integer and calculate c using
    # Pythagorean theorem formula
    if (type(a) == int and type(b) == int):

        # Pythagorean theorem formula
        c = math.sqrt(a * a + b * b)

        # Check if c is an integer, then  set flag variable to "True"
        if c % 1 == 0:

            result = True

    return result

# Testing if 3 and 4 is a pithagorean pair. The result is "True"
# print(pythagorean_pair(3,4))

# Testing if 6 and 7 is a pithagorean pair. The result should be "False"
# print(pythagorean_pair(6,9))
