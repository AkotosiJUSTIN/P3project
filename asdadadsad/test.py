import random
import time

import asyncio

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
        num1 = random.randint(0, 11)
        num2 = random.randint(0, 11)
    elif difficulty == "moderate":
        num1 = random.randint(11, 101)
        num2 = random.randint(11, 101)
    elif difficulty == "hard":
        num1 = random.randint(101, 501)
        num2 = random.randint(101, 501)
    else:
        raise ValueError("Invalid difficulty level.")

    equation = f"{num1} {operator} {num2}"
    return equation

async def timer(seconds):
  start_time = time.time()
  while time.time() - start_time < seconds:
    await asyncio.sleep(0.1)
  raise asyncio.TimeoutError

async def play_game(difficulty: str, equation_type: str) -> None:
  num_problems = get_valid_num_problems()
  correct_answers = 0
  incorrect_answers = 0

  while num_problems > 0:
    equation = generate_math_equation(difficulty, equation_type)

    # Start the timer.
    timer_task = asyncio.create_task(timer(10))

    # Get the user's input.
    answer = await asyncio.create_task(input("What is the answer? "))

    # Cancel the timer if the user enters an answer.
    timer_task.cancel()

    # Evaluate the equation and answer.
    evaluated_equation = eval(equation)
    evaluated_answer = eval(answer)

    if evaluated_equation == evaluated_answer:
      correct_answers += 1
    elif evaluated_equation != evaluated_answer:
      incorrect_answers += 1
      num_problems -= 1

  # Display the score after completing all the problems.
  print(f"Your score is {correct_answers} / {correct_answers + incorrect_answers + num_problems}")

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