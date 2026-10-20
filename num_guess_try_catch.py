#!/usr/bin/env python3
# Created by: Adrian student
# Created on: 19th Oct 2026
# This program uses a random number generator to choose a
# random number and then asks the user to try guessing it
import random


def main():
    # set up the random number generator
    number = int(random.randint(0, 9))

    # get the user guess between 0 and 9 
    user_input = input("Enter your guess number : ")
    print("")

    # get the user guess and check if it is correct
    try:
        # cast the user input into an integer 
        user_number = int(user_input)

        # check if the user guess is correct
        if user_number == number:
            print("you guessed correctly !!")
        else:
                print("you guessed wrong!!")
                print("The correct answer was : {}".format(number))
    except ValueError:
        print("{} is not an integer".format(user_input))
        # Add the finally block
    finally:
        print("Thank you for playing ")


if __name__ == "__main__":
    main()
