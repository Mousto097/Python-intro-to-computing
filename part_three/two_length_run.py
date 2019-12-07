# Author: Mamadou Bah


def two_length_run(new_list):
    '''Returns True if the given list has is at least one run (of length at least two)'''

    number_of_positive_elements = 0
    for val in range(len(new_list)-1):
        if new_list[val] == new_list[val+1]:
            return True

    return False


def mainProgram():

    # Ask the user for a list of numbers
    raw_input = input(
        "Please input a list of numbers separated by space: ").strip().split()

    # Create a new list that is list of equivalent numbers entered by the user
    new_list = []
    for num in raw_input:
        new_list.append(float(num))

    # Function call and result printing
    result = two_length_run(new_list)
    print(result)


mainProgram()
