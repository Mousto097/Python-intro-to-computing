# Author: Mamadou Bah


def computes_vote_percentage(user_char):

    num_of_yes = 0
    num_of_no = 0

    # Double the element of the reversed char
    for char in user_char:
        if char == 'yes':
            num_of_yes += 1
        if char == 'no':
            num_of_no += 1

    # Compute percentage of 'yes'
    percentage = (num_of_yes)/(num_of_yes+num_of_no)

    return percentage


def mainProgram():

    # Ask the user for a chain of characters
    user_input = input(
        'Input the votes (yes, no, or abstention) separated by spaces, then push enter: ').strip().split()

    # Create a new list to reformat the user input
    new_list = []
    for char in user_input:
        new_list.append(char)

    # Function call and result printing
    result = computes_vote_percentage(user_input)
    print("the percentage of yes is:", result*100, "%")

    # Displaying appropriate message based on the percentage of 'yes'
    if(result == 1):
        print("unanimous")
    elif(1 > result and result >= (2/3)):
        print("clear majority")
    elif((2/3) > result and result >= (1/2)):
        print("simple majority")
    else:
        print("the motion failed")


mainProgram()
