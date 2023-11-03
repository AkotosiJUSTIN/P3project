import random
import time

equation_type_to_operator_map = {
    "add": "+",
    "subtract": "-",
    "multiply": "*",
    "divide": "/",
}

def generate_math_equation(difficulty: str, equation_type: str) -> str:
    """Generates a random math equation based on the given difficulty and equation type.

    Args:
        difficulty: A string representing the difficulty level, either "easy", "moderate", or "hard".
        equation_type: A string representing the equation type, either "add", "subtract", "multiply", or "divide".

    Returns:
        A string representing the math equation.
    """

    operator = equation_type_to_operator_map[equation_type]

    if difficulty == "easy":
        # Generate a random single-digit number.
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
    elif difficulty == "moderate":
        # Generate a random two-digit number.
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
    elif difficulty == "hard":
        # Generate a random three-digit number.
        num1 = random.randint(100, 999)
        num2 = random.randint(100, 999)
    else:
        raise ValueError("Invalid difficulty level.")

    # Generate the math equation.
    equation = f"{num1} {operator} {num2}"

    # Return the math equation as a string.
    return equation

def play_game(difficulty: str, equation_type: str) -> None:
  """Plays the math game.

  Args:
    difficulty: A string representing the difficulty level, either "easy", "moderate", or "hard".
    equation_type: A string representing the equation type, either "add", "subtract", "multiply", or "divide".
  """

  # Generate a random math equation based on the chosen difficulty and equation type.
  equation = generate_math_equation(difficulty, equation_type)

  # Set the answer count to 0.
  answer_count = 0

  # Print the equation and ask the user to solve it.
  print(equation)

  # If the difficulty is hard, set a timer of 10 seconds.
  if difficulty == "hard":
    timer = 10
    start_time = time.time()

  # While the answer count is less than 3 (or the difficulty is easy or moderate), ask the user for an answer.
  while answer_count < 3 and (difficulty in ["easy", "moderate"] or timer > 0):

    # If the difficulty is hard, print the remaining time.
    if difficulty == "hard":
      print(f"Time remaining: {timer:.2f} seconds")

    # Ask the user for an answer.
    answer = input("What is the answer? ")

    # Increment the answer count.
    answer_count += 1

    # Evaluate the equation and the answer separately.
    evaluated_equation = eval(equation)
    evaluated_answer = eval(answer)

    # Check if the answer is correct.
    if evaluated_equation == evaluated_answer:
      print("Correct!")
      break
    else:
      print("Incorrect.")

    # If the difficulty is hard, calculate the remaining time.
    if difficulty == "hard":
      remaining_time = timer - (time.time() - start_time)

      # If the timer ran out, tell the user.
      if remaining_time <= 0:
        print("Out of time!")
        break

      # Set the timer to the remaining time.
      timer = remaining_time

    # If the answer count is equal to 3, tell the user that they ran out of tries and break out of the loop.
    if answer_count == 3:
      print("You ran out of tries.")
      break

  # Ask the user if they want to play again.
  play_again = input("Do you want to play again? (y/n): ")
  if play_again == "y":
    play_game(difficulty, equation_type)

# Start the game.
print("Welcome to the math game!")

# Prompt the user to choose a difficulty level.
difficulty = input("Choose a difficulty level (easy, moderate, or hard): ")

# Prompt the user to choose an equation type.
equation_type = input("Choose an equation type (add, subtract, multiply, or divide): ")

# Play the game.
play_game(difficulty, equation_type)