# Author: Mamadou Bah


def find_minimum_number_of_coins():
    "Print the minimum number of coins with which that amount can be made"

    # Take input from user for the amount of money he/she is owed (in dollars)
    amount_owed = float(input("Enter the amount you are owed in $: "))*100

    # The available coins (in cents):
    quarter = 25
    dime = 10
    nickel = 5
    penny = 1

    # The number of coins owed to the customer
    number_of_coins = 0

    if (amount_owed >= quarter):

        number_of_coins = number_of_coins + (amount_owed//quarter)
        amount_owed = int(amount_owed % quarter)

    if(amount_owed >= dime):

        number_of_coins = number_of_coins + (amount_owed//dime)
        amount_owed = amount_owed % dime

    if(amount_owed >= nickel):

        number_of_coins = number_of_coins + (amount_owed//nickel)
        amount_owed = amount_owed % nickel

    if(amount_owed >= penny):

        number_of_coins = number_of_coins + (amount_owed//penny)

    print("The minimum number of coins the cashier can return is:",
          int(number_of_coins), "coins")


# Testing if the program print the minimum number of coins with which that amount can
# be made. The result should be: 4 coins
# Test case: amount_owed = $ 0.56
# find_minimum_number_of_coins()

# Testing if the program print the minimum number of coins with which that amount can
# be made. The result should be: 9 coins
# Test case: amount_owed = $ 1.42
# find_minimum_number_of_coins()

# Testing if the program print the minimum number of coins with which that amount can
# be made. The result should be: 4 coins
# Test case: amount_owed = $ 1.00
# find_minimum_number_of_coins()
