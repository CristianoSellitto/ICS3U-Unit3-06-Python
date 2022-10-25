#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in October 2022
# A program that finds if the user's number between 0 and 9 is equal to the random number

import random


def main():
    # Finds if the chosen number from 0 to 9 is equal to the random number

    random_number = random.randint(0, 9)
    chosen_number = input("Enter a number from 0-9: ")
    try:
        chosen_int = int(chosen_number)
        if chosen_int == random_number:
            print("\nYou got the number right!")
        else:
            print("\nYou got the number wrong.")
        print("The number was {}.".format(random_number))
    except ValueError:
        print("\nThis isn't an integer")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
