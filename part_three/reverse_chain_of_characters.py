# Author: Mamadou Bah


def reverse_chain_of_characters(user_char):

    # Reversing the chain of characters
    reversed_char = user_char[::-1]

    # Double the element of the reversed char
    result = ''
    for char in reversed_char:
        result = result + (char*2)

    return result


def mainProgram():

    # Ask the user for a chain of characters
    user_input = input('Please enter a chain of characters: ')

    # Function call and result printing
    result = reverse_chain_of_characters(user_input)
    print(result)


mainProgram()
