# Author: Mamadou Bah


def increment_array_elements_by_one(array):
    '''
    (list) -> list
    This function takes an array and modifies it by adding 1 to all the elements.
    Preconditions: array is a reference to an nxn array that contains integers
    '''

    # Adding 1 to all the elements.
    row = 0
    while row < len(array):
        col = 0
        while col < len(array[row]):
            array[row][col] = array[row][col] + 1
            col = col + 1
        row = row + 1
    return array


def increment_array_elements_by_one_v2(array):
    '''
    (list) -> list
    This function takes takes an array and returns a new array containing the values of the given array provided as a parameter incremented by 1, without modifying it.
    Preconditions: array is a reference to an nxn array that contains integers
    '''

    # Create new array
    new_array = []

    # Returns a new array containing the values of
    # the given array provided as the parameter
    new_array = [row[:] for row in array]

    # Add 1 to all the elements of the new array.
    row = 0
    while row < len(new_array):
        col = 0
        while col < len(new_array[row]):
            new_array[row][col] = new_array[row][col] + 1
            col = col + 1
        row = row + 1
    return new_array


def mainProgram():
    '''
    This function ask the user to input an array, call the function add and display the modified array. 
    Then call the function add_V2, with the array as a parameter, and display its resulting array. 
    Finally display the original array to check that it has not changed
    '''

    # Ask the user to input an array
    print("Enter the number of columns, with spaces.")
    print("A row per line, and an empty line at the end.")
    matrix = []
    while True:
        line = input()
        if not line:
            break
        values = line.split()
        row = [int(val) for val in values]
        matrix.append(row)

    # Display the array created by the user
    print("The array is:")
    print(matrix)

    # Call the function add and display the modified array.
    result1 = increment_array_elements_by_one(matrix)
    print("\nAfter executing the function add, the array is:")
    print(result1)

    # Then call the function add_V2, with the array as a parameter, and display its resulting array.
    result2 = increment_array_elements_by_one_v2(matrix)
    print("\nA new array created with add_V2:")
    print(result2)

    # Display the original array to check that it has not changed
    print("\nAfter executing the function add_V2, the initial array is:")
    print(matrix)


mainProgram()
