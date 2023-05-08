#!/usr/bin/env python3
import random

import prompt


def main():
    name = prompt.string('May I have your name? ')
    answers_count = 0
    print(f"Hello, {name}!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    for i in range(1, 4):
        number = random.randint(0, 100)
        print(f"Question: {number}")
        print("Your answer: ")
        answer = input()
        if number % 2 == 0 and answer.lower() == "yes":
            print("Correct!")
            answers_count += 1
            continue
        elif number % 2 == 0 and answer.lower() == "no":
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\n Let's try again, {name}!")
            continue
        elif number % 2 != 0 and answer.lower() == "no":
            print("Correct!")
            answers_count += 1
            continue
        elif number % 2 != 0 and answer.lower() == "yes":
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            continue
        else:
            print("Incorrect input")

    if answers_count == 3:
        print(f"Congratulations, {name}")
    else:
        print("Sorry, try again! I believe in you! <3")


if __name__ == '__main__':
    main()
