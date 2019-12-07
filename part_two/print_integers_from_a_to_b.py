# Author: Mamadou Bah


def print_integers_from_a_to_b(a, b):
    '''Prints integers from a to b
    Expected result is: a, a+1, a+2, ..., b'''

    start = a
    stop = b+1

    for number in range(start, stop):
        print(number, end=", ")


a = int(input("Please prvide a value for a: "))
b = int(input("Please prvide a value for b: "))
print_integers_from_a_to_b(a, b)
