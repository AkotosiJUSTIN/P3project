import tkinter as tk
from tkinter import messagebox
import random
import time

# Function to display text on the screen
def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to ask the user for the desired difficulty
def ask_difficulty():
    return input_difficulty.get()

# Function to ask the user for the desired operations
def ask_operations():
    return input_operations.get().split(',')

# Function to ask the user how many questions they want to answer
def ask_question_count():
    return int(input_question_count.get())

# Function to check if the user's answer is correct
def check_answer(user_answer, correct_answer):
    return user_answer == correct_answer

# Function to run the game
def run_game():
    global input_difficulty, input_operations, input_question_count, input_user_answer

    pygame.display.set_caption("Math Game")
    running = True
    clock = pygame.time.Clock()

    # Get user inputs
    difficulty = ask_difficulty()
    operations = ask_operations()
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

        # Check if the user's answer is correct
        if check_answer(input_user_answer.get(), correct_answer):
            correct_answers += 1
        else:
            incorrect_answers += 1

        # Check if the user has answered all the questions
        if correct_answers + incorrect_answers == question_count:
            running = False

        # Update display
        pygame.display.flip()
        clock.tick(60)

# Initialize tkinter window
window = tk.Tk()
window.title("Math Game")

# Create input fields and labels
label_difficulty = tk.Label(window, text="Difficulty:")
label_difficulty.pack()
input_difficulty = tk.Entry(window)
input_difficulty.pack()

label_operations = tk.Label(window, text="Operations (comma-separated):")
label_operations.pack()
input_operations = tk.Entry(window)
input_operations.pack()

label_question_count = tk.Label(window, text="Question count:")
label_question_count.pack()
input_question_count = tk.Entry(window)
input_question_count.pack()

label_user_answer = tk.Label(window, text="Your answer:")
label_user_answer.pack()
input_user_answer = tk.Entry(window)
input_user_answer.pack()

button_start = tk.Button(window, text="Start", command=run_game)
button_start.pack()

# Run the tkinter window's main loop
window.mainloop()

pygame.quit()