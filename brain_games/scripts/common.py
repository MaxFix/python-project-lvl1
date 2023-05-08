def correct_answer(answers_count=None):
    print("Correct!")
    answers_count += 1
    return answers_count


def end_of_game(name="", answers_count=None):
    if answers_count == 3:
        print(f"Congratulations, {name}")
    else:
        print("Sorry, try again! I believe in you! <3")
