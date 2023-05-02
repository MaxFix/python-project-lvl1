#!/usr/bin/env python3
import random

import prompt


def main():
    name = prompt.string('May I have your name? ')
    answers_count = 0
    print(f"Hello, {name}!")
    print("What is the result of the expression?")

    for i in range(1, 4):
        number1 = random.randint(0, 100)
        number2 = random.randint(0, 100)
        correct_result = int(number2 + number1)
        print(f"Question: {number1} + {number2}")
        print("Your answer: ")
        answer = int(input())
        if answer == correct_result:
            print("Correct!")
            answers_count += 1
            continue
        elif answer != correct_result:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_result}'.")
            print(f"Let's try again, {name}!")
            continue
        else:
            print("Incorrect input")
    if answers_count == 3:
        print(f"Congratulations, {name}")
    else:
        print("Sorry, try again! I believe in you! <3")