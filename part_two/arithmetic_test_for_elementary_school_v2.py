import random

# Author: Mamadou Bah


def doTest(operation):
    '''The user is tested with 10 questions that are randomly distributed between multiplication and addition'''

    result = False

    # Randomly generates two-positive one-digit integers
    first_number = random.randint(0, 9)
    second_number = random.randint(0, 9)

    # Perform addition or multiplication
    if(operation == 0):

        # Compute correct answer
        correct_answer = first_number + second_number

        # Get the student answer
        student_answer = int(
            input("How much is " + str(first_number) + " + " + str(second_number) + "? "))

    else:

        # Compute correct answer
        correct_answer = first_number * second_number

        # Get the student answer
        student_answer = int(input(
            "What is " + str(first_number) + " x " + str(second_number) + " equal to "))

    # Returns true if the user has answered the question correctly and false if not
    if (student_answer == correct_answer):
        result = True
    else:
        print("Wrong answer! The correct answer is:", correct_answer)

    return result


responsesCorrect = 0
print("The software will process a test with 10 questions …… ")
for compteur in range(10):
    operation = random.randint(0, 1)
    print("\nQuestion number", compteur, ".")
    if doTest(operation) == True:
        responsesCorrect += 1
print("\n", responsesCorrect, "Correct responses")
if responsesCorrect <= 6:
    print(" Ask some help from your instructor.")
else:
    print(" Congratulations!")
