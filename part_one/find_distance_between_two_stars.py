# Author: Mamadou Bah


# Function for part A
def convert_sideral_years_into_seconds():
    "Converts a given number of sidereal years into seconds"

    # Take input from user for the number of light-years
    number_of_light_years = float(input("Input a number of light-years: "))

    # Conversion of a given number of sidereal years into seconds

    number_of_seconds = number_of_light_years*365.26*24*60*60

    print("The number of seconds is:", number_of_seconds)


# Function for part B
def transform_seconds_into_distance():
    # -------------------------------- Part A -----------------------------------------
    "Converts a given number of sidereal years into seconds"

    # Take input from user for the number of light-years
    number_of_light_years = float(input("Input a number of light-years: "))

    # Conversion of a given number of sidereal years into seconds

    number_of_seconds = number_of_light_years*365.26*24*60*60

    print("The number of seconds is:", number_of_seconds)

    # -------------------------------- Part B -----------------------------------------
    # Conversion of number of seconds into a distance

    distance = number_of_seconds*300000

    print("The distance is", distance, "km")


# Function for part C
def find_distance_between_two_stars():
    # -------------------------------- Part A -----------------------------------------
    "Converts a given number of sidereal years into seconds"

    # Take input from user for the number of light-years
    number_of_light_years = float(input("Input a number of light-years: "))

    # Conversion of a given number of sidereal years into seconds

    number_of_seconds = number_of_light_years*365.26*24*60*60

    print("The number of seconds is:", number_of_seconds)

    # -------------------------------- Part B -----------------------------------------
    # Conversion of number of seconds into a distance

    distance = number_of_seconds*300000

    print("The distance is", distance, "km")

    # -------------------------------- Part C -----------------------------------------
    "Find the distance (in kilometers) traveled by a communication signal from one star to another via Earth"

    # Take input from user for the distances between each star and Earth (in light-years)
    distance_for_first_star = float(
        input("Input the distance to the first star, in light years: "))
    distance_for_second_star = float(
        input("Input the distance to the second star, in light years: "))

    # Compute the distance between the first star and the earth
    number_of_seconds_first_star = distance_for_first_star*365.26*24*60*60
    distance_first_star_to_earth = number_of_seconds_first_star*300000

    # Compute the distance between the second star and the earth
    number_of_seconds_for_second_star = distance_for_second_star*365.26*24*60*60
    distance_second_star_to_earth = number_of_seconds_for_second_star*300000

    # Compute the distance between the first star and the second star
    total_distance = distance_first_star_to_earth+distance_second_star_to_earth

    print("The distance between the two stars is", total_distance, "km")


# Test function
find_distance_between_two_stars()
