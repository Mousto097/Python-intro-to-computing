# Author: Mamadou Moustapha Bah (8851762)


def longest_run(new_list):
    '''Takes a list of numbers and returns the length of the longest run'''

    max_result = 0

    if(len(new_list) != 0):
        result = 1
        last_seen = new_list[0]

        for v in new_list[1:]:
            if v == last_seen:
                result += 1
            else:
                if result > max_result:
                    max_result = result
                last_seen = v
                result = 1

        # In case the longest sequence would be at the end of the list
        if result > max_result:
            max_result = result

    return max_result


def mainProgram():

    # Ask the user for a list of numbers
    raw_input = input(
        "Please input a list of numbers separated by space: ").strip().split()

    # Create a new list that is list of equivalent numbers entered by the user
    new_list = []
    for num in raw_input:
        new_list.append(float(num))

    # Function call and result printing
    result = longest_run(new_list)
    print(result)


mainProgram()
