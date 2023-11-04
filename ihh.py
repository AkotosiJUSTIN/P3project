import random
import time

equation_type_to_operator_map = {
    "add": "+",
    "subtract": "-",
    "multiply": "*",
    "divide": "/",
}

def get_valid_difficulty():
    while True:
        difficulty = input("Choose a difficulty level (easy, moderate, or hard): ")
        if difficulty in ["easy", "moderate", "hard"]:
            return difficulty
        else:
            print("Invalid input. Try again.")

def get_valid_equation_type():
    while True:
        equation_type = input("Choose an equation type (add, subtract, multiply, or divide): ")
        if equation_type in ["add", "subtract", "multiply", "divide"]:
            return equation_type
        else:
            print("Invalid input. Try again.")

def get_valid_num_problems():
    while True:
        try:
            num_problems = int(input("How many problems do you want to solve? "))
            if num_problems > 0:
                return num_problems
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def generate_math_equation(difficulty: str, equation_type: str) -> str:
    operator = equation_type_to_operator_map[equation_type]

    if difficulty == "easy":
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
    elif difficulty == "moderate":
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
    elif difficulty == "hard":
        num1 = random.randint(100, 999)
        num2 = random.randint(100, 999)
    else:
        raise ValueError("Invalid difficulty level.")

    equation = f"{num1} {operator} {num2}"
    return equation

def play_game(difficulty: str, equation_type: str) -> None:
    num_problems = get_valid_num_problems()
    correct_answers = 0
    incorrect_answers = 0

    while num_problems > 0:
        equation = generate_math_equation(difficulty, equation_type)

        if difficulty == "easy":
            answer_limit = 1
        else:
            answer_limit = 3

        print(equation)

        if difficulty == "hard":
            timer = 10
            start_time = time.time()

        while answer_limit > 0 and (difficulty in ["easy", "moderate"] or (difficulty == "hard" and timer > 0)):
            if difficulty == "hard":
                print(f"Time remaining: {timer:.2f} seconds")

            answer = input("What is the answer? ")

            evaluated_equation = eval(equation)
            evaluated_answer = eval(answer)

            if evaluated_equation == evaluated_answer:
                correct_answers += 1
                break
            elif evaluated_equation != evaluated_answer:
                incorrect_answers += 1
                answer_limit -= 1
                continue

            if difficulty == "hard":
                remaining_time = timer - (time.time() - start_time)

                if remaining_time <= 0:
                    print("Out of time!")
                    break

                timer = remaining_time

        num_problems -= 1

    # Display the score after completing all the problems.
    print(f"Your score is {correct_answers} / {correct_answers + incorrect_answers}")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again == "y":
        play_game(difficulty, equation_type)

# Start the game.
print("Welcome to the math game!")

# Prompt the user to choose a difficulty level.
difficulty = get_valid_difficulty()

# Prompt the user to choose an equation type.
equation_type = get_valid_equation_type()

# Play the game.
play_game(difficulty, equation_type)
