# Author: Mamadou Bah


def erasTable(tab):
    '''
    (list) -> None
    This function prepares the game table (array)
    by putting '-' in all the elements.
    It does not create a new array
    Preconditions: tab is a reference to an nxn array matrice n x n that contains '-', 'X' or 'O'
    '''

    # to complete
    # returns nothing
    row = 0
    while row < len(tab):
        col = 0
        while col < len(tab[row]):
            tab[row][col] = '-'
            col = col + 1
        row = row + 1


def verifyWin(tab):
    '''(list) ->  bool
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    * Verify if there is a winner.
    * Look for 3 X's and O's in a row, column, and diagonal.
    * If we find one, we display the winner (the message "Player X has won"
    * or "Player O has won!") and returns True.
    * If there is a draw (verify it with the function testdraw),
    * display "It is a draw" and returns True.
    * If the game is not over, returns False.
    * The function call the functions testrows, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Those functions returns the winner 'X' or 'O', or '-' if there is no winner.
    '''

    # Look for 3 X's in a row, column, and diagonal.
    if(testLignes(tab) == 'X' or testCols(tab) == 'X' or testDiags(tab) == 'X'):

        # If it is the case, we print the appropriate message
        print("\n>>>>>>>>>>Player X has won!!!<<<<<<<<<<")
        return True

    # Look for 3 O's in a row, column, and diagonal.
    if(testLignes(tab) == 'O' or testCols(tab) == 'O' or testDiags(tab) == 'O'):

        # If it is the case, we print the appropriate message
        print("\n>>>>>>>>>>Player O has won!!!<<<<<<<<<<")
        return True

    # Check there is a draw using the testdraw function
    if(testDraw(tab) == True):

        # If it is the case, we print the appropriate message
        print("It is a draw")
        return True

    # If the game is not over, returns False.
    else:
        return False


def testLignes(tab):
    ''' (list) ->  str
    * verify if there is a winning row.
    * Look for three 'X' or three 'O' in a row.
    * If they are found, the character 'X' or 'O' is returned, otherwise '-' is returned.
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    '''

    # Variable that hold the character of the winner
    winner = '-'
    for i in range(3):
        # Check the 3 existing lignes to find three 'X' or three 'O'
        if tab[i][0] == tab[i][1] == tab[i][2] and tab[i][0] != "-":
            # If it is the case, the character 'X' or 'O' is returned
            winner = tab[i][0]
            # Stop the loop, cause we found three 'X' or three 'O'
            break
    return winner


def testCols(tab):
    ''' (list) ->  str
    * verify a winning column.
    * look for three 'X' or three 'O' in a column.
    * If it is the case the character 'X' or 'O' is returned, otherwise '-' is returned.
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    '''

    # Variable that hold the character of the winner
    winner = '-'
    for i in range(3):
        # Check the 3 existing columns to find three 'X' or three 'O'
        if tab[0][i] == tab[1][i] == tab[2][i] and tab[0][i] != "-":
            # If it is the case, the character 'X' or 'O' is returned
            winner = tab[0][i]
            # Stop the loop, cause we found three 'X' or three 'O'
            break
    return winner


def testDiags(tab):
    ''' (list) ->  str
    * Look for three 'X' or three 'O' in a diagonal.
    * If it is the case, the character 'X' or 'O' is returned
    * otherwise '-' is returned.
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    '''
    # Variable that hold the character of the winner
    winner = '-'
    if tab[1][1] != "-":
        # Check the two existing diagonals to find three 'X' or three 'O'
        if (tab[0][0] == tab[1][1] == tab[2][2]
                or tab[0][2] == tab[1][1] == tab[2][0]):
            # If it is the case, the character 'X' or 'O' is returned
            winner = tab[1][1]
    return winner


def testDraw(tab):
    ''' (list) ->  bool
    * verify if there is a draw
    * check if all the array elements have X or O, not '-'.
    * If we do not find find any '-' in the array, return True.
    * If there is any '-', return false.
    * Preconditions: tab is a reference to an nxn array that contains '-', 'X' or 'O'
    '''

    # Go through each rows
    row = 0
    while row < len(tab):
        # Go through each columns
        col = 0
        while col < len(tab[row]):
            # If there is any '-', return false.
            if tab[row][col] == '-':
                return False
            col = col + 1
        row = row + 1
    # If we do not find find any '-' in the array, return True.
    return True
