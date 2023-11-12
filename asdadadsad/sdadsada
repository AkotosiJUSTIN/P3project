import pygame
import random
import time

# Initialize pygame
pygame.init()

# Create a font object
font = pygame.font.Font(None, 36)

# Create a screen object
screen = pygame.display.set_mode((640, 480))

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Function to display text on the screen
def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to ask the user for the desired difficulty
def ask_difficulty():
    return input("Choose your difficulty: easy, moderate, or hard. ")

# Function to ask the user for the desired operations
def ask_operations():
    return input("Choose the operations you want to use: add, subtract, multiply, or divide. Separate them with commas. ")

# Function to ask the user how many questions they want to answer
def ask_question_count():
    return int(input("How many questions do you want to answer? "))

# Function to check if the user's answer is correct
def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

# Function to run the game
def run_game():
    pygame.display.set_caption("Math Game")
    running = True
    clock = pygame.time.Clock()

    # Get user inputs
    difficulty = ask_difficulty()
    operations = ask_operations().split(',')
    question_count = ask_question_count()

    # Initialize score variables
    correct_answers = 0
    incorrect_answers = 0

    # Generate random numbers for each operation
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)

    # Start game loop
    while running:
        screen.fill(WHITE)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update display text
        display_text("Correct answers: " + str(correct_answers), GREEN, 10, 10)
        display_text("Incorrect answers: " + str(incorrect_answers), RED, 10, 50)

        # Get user input for the answer
        user_answer = input("What is the result of " + str(num1) + " " + operations[0] + " " + str(num2) + "? ")

        # Check if the user's answer is correct
        if check_answer(user_answer, correct_answer):
            correct_answers += 1
        else:
            incorrect_answers += 1

        # Check if the user has answered all the questions
        if correct_answers + incorrect_answers == question_count:
            running = False

        # Update display
        pygame.display.flip()
        clock.tick(60)

run_game()
pygame.quit()
