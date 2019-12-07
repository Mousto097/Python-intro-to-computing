import random

# Author: Mamadou Bah


def performTest(operation):
    ''' Execute the arithmetic test for a student for multiplication or addition operations 
      and return the number of correct answers '''

    correctCounts = 0

    # Test the student with exactly 10 questions

    for i in range(1, 11):

        # Part a) Randomly generates two-positive one-digit integers
        first_number = random.randint(0, 9)
        second_number = random.randint(0, 9)

        # Part b) Ask the student to enter the answer for the arithmetic operation of the two numbers

        print("\nQuestion number", i, ".")

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

        # Part c) Check if the result is correct. If the answer is incorrect, provides the correct answers

        if (student_answer == correct_answer):
            correctCounts = correctCounts + 1
            print("Correct answer!")

        else:
            print("Incorrect answer! the correct answer is:", correct_answer)

    return correctCounts


print("This software tests you with 10 questions …… ")
operation = int(
    input("0) Addition \n1) Multiplication\nPlease make a selection (0 or 1): "))

correctCounts = performTest(operation)

print("\n", correctCounts, "Correct responses")
if correctCounts <= 6:
    print(" Please ask your teacher for help.")
else:
    print(" Congratulations!")
