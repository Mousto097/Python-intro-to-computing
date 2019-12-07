# Author: Mamadou Bah


def count_positive_elements(new_list):

    # Counter for the number of positive element
    number_of_positive_elements = 0
    for nb in range(len(new_list)):
        if new_list[nb] > 0:
            number_of_positive_elements = number_of_positive_elements + 1

    # Returns the number of positive elements
    return number_of_positive_elements


def mainProgram():

    # Ask the user for a list of numbers
    raw_input = input(
        "Please input a list of numbers separated by space: ").strip().split()

    # Create a new list that is list of equivalent numbers entered by the user
    new_list = []
    for num in raw_input:
        new_list.append(float(num))

    # Function call and result printing
    result = count_positive_elements(new_list)
    print("There are", result, "positive numbers in your list.")


mainProgram()
