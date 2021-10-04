# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Oct 2021
# This program asks the user to pick a number between 0-9 and guess correctly


import random


def main():
    # this function loops until it exits out of a break if 
    # the user guesses correctly, otherwise it loops back for the user to
    # restart guessing

    # input
    dice = random.randint(0, 9)  # a number between 0 and 9
    user_number = input("Enter in a positive integer: ")
    print("")

    # process & output
    try:

        user_number_int = int(user_number)

        while True:
            if user_number_int < 0:
                print("That is an invalid answer.")
            else:
                if user_number_int == dice:
                    print("You guessed right!")
                    break

                if user_number_int < dice:
                    print("You guessed too low.")

                if user_number_int > dice:
                    print("You guessed too high!")

            user_number = input("Try again: ")

            user_number_int = int(user_number)

    except Exception:
        print("That is an invalid answer.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
