# Author: Mamadou Bah


def compute_the_bmi(p, t):
    ''' Calculate the BMI using the weight and the height'''

    # BMI formula = weight/(height)^2
    r = p/(t**2)

    # return the BMI value calculated
    return r


def print_descriptive_message_based_on_bmi_level(r):
    ## Print a message describing the BMI based on the value returned ##

    if(r < 18.5):
        print("underweight")

    elif(18.5 <= r and r < 25):
        print("normal weight")

    elif(25 <= r and r < 30):
        print("overweight")

    else:
        print("obese")


p = float(input("Enter your weight in kilograms "))
t = float(input("Enter your height in meters "))

r = compute_the_bmi(p, t)
print("Your BMI is", r)
print_descriptive_message_based_on_bmi_level(r)
