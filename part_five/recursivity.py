# Author: Mamadou Bah


def stars(number):
    '''(int) -> None
        This recursive function take as a parameter a non negative integer and will 
        generate a drawing composed of stars.'''

    print('*'*number)
    if number > 1:
        stars(number-1)
    print('*'*number)

# Please uncomment the next line to test my function (code)
# stars(4)


def sumListPos_rec(list, size):
    '''(list, int) -> int
        This recursive function take as parameter a list and as a second parameter the number of 
        the list elements, and that will return the sum of the positive elements (> 0).'''

    if size == 0:
        return 0
    else:
        if(list[0] > 0):
            return list[0]+sumListPos_rec(list[1:], size-1)
        else:
            return sumListPos_rec(list[1:], size-1)

# Please uncomment the next line to test my function (code)
# l = [1, -2, 5, 0, -5]
# print(sumListPos_rec(l, len(l)))
