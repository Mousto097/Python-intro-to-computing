# Author: Mamadou Bah


def convert_romans_to_integers_v1(roman_number):

    result1 = 0

    roman_number = roman_number.upper()

    # Using a method that applies to chain of characters (of type str).
    countM = roman_number.count('M')
    countD = roman_number.count('D')
    countC = roman_number.count('C')
    countX = roman_number.count('X')
    countV = roman_number.count('V')
    countI = roman_number.count('I')

    # Accumulate the values of all the symbols.
    result1 = (countM*1000)+(countD*500)+(countC*100) + \
        (countX*10)+(countV*5)+(countI*1)

    return result1


def convert_romans_to_integers_v2(roman_number):

    result2 = 0

    countM = 0
    countD = 0
    countC = 0
    countX = 0
    countV = 0
    countI = 0

    # Without using methods of the class str.
    for char in roman_number:

        if(char == 'M'):
            countM += 1
        if(char == 'D'):
            countD += 1
        if(char == 'C'):
            countC += 1
        if(char == 'X'):
            countX += 1
        if(char == 'V'):
            countV += 1
        if(char == 'I'):
            countI += 1

    # Accumulate the values of all the symbols.
    result2 = (countM*1000)+(countD*500)+(countC*100) + \
        (countX*10)+(countV*5)+(countI*1)

    return result2


def mainProgram():

    # Ask the user for a chain of characters
    user_input = input(
        'Input a roman number using the letters M, D, C, X and I: ')

    # Call function and display result
    result1 = convert_romans_to_integers_v1(user_input)
    print("roman_v1 result is:", result1)

    # Call function and display result
    result2 = convert_romans_to_integers_v2(user_input)
    print("roman_v2 result is:", result2)


mainProgram()
