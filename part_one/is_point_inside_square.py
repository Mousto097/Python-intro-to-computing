# Author: Mamadou Bah


def is_point_inside_square(xs, ys, side):
    "Print 'True' if the given query point is inside of the given square, otherwise it should print 'False'"

    # Make sure that "side" is a non-negative
    if (side >= 0):

        # "result" is the flag variable and is set to False at the begining
        result = False

        # Take input from user for  the x and y coordinates of some query point
        x_coordinate = float(
            input("Enter a number for the x coordinate of a query point: "))
        y_coordinate = float(
            input("Enter a number for the y coordinate of a query point: "))

        # Make sure that x is between xs and side
        is_between_xs_and_side = xs <= x_coordinate and x_coordinate <= side
        # Make sure that y is between ys and side
        is_between_ys_and_side = ys <= y_coordinate and y_coordinate <= side

        # If xs < x < side and ys < y < side, then the query point (x,y) is within given square
        if (is_between_xs_and_side and is_between_ys_and_side):

            result = True

    else:
        print("side should be a non-negative number")

    print(result)

# Testing  if the given query point is inside of the given square. The result should be "True"
# Test case: enter x_coordinate = 0 and y_coordinate = 1.2
# is_point_inside_square(0, 0, 2.5)

# Testing  if (-1, 1.5) is inside of the given square. The result should be "False"
# Test case: enter x_coordinate = -1 and y_coordinate = 1.5
# is_point_inside_square(2.5, 1, 1)
