import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import time

# Dictionary of operator type
operator_type = {"add": "+", "subtract": "-", "multiply": "*", "divide": "/"}

# GUI initialization
root = tk.Tk()
root.title("Math Mastermind")
root.geometry("300x200")


#text on top of the drawer
difficulty_label = tk.Label(root, text="Choose a difficulty level:")
difficulty_label.pack()

#drawer of difficulties
difficulty_var = tk.StringVar()
difficulty_var.set("easy")
difficulty_menu = tk.OptionMenu(root, difficulty_var, "easy", "moderate", "hard")
difficulty_menu.pack()

#text on top of the drawer
equation_label = tk.Label(root, text="Choose an equation type:")
equation_label.pack()

#drawer of equations
equation_var = tk.StringVar()
equation_var.set("add")
equation_menu = tk.OptionMenu(root, equation_var, "add", "subtract", "multiply", "divide")
equation_menu.pack()

#text on top of the drawer
num_problems_label = tk.Label(root, text="Enter the number of problems:")
num_problems_label.pack()

#box that user can put their answer about how many problems they want to answer
num_problems_entry = tk.Entry(root)
num_problems_entry.pack()

# Button to start the game
def start_game():
    difficulty = difficulty_var.get()
    equation_type = equation_var.get()

    try:
        score = int(num_problems_entry.get())
        if score <= 0:
            messagebox.showerror("Error", "Please enter a positive number.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
        return

    # Hide the main window
    root.withdraw()
    play_game(difficulty, equation_type, score)

play_button = tk.Button(root, text="Play Game", command=start_game)
play_button.pack()

def play_game(difficulty, equation_type, score):
    num_problems = score
    correct_answer = 0

    while num_problems > 0:
        equation = make_equation(difficulty, equation_type)

        #limit answers and timer of 10 seconds fo hard difficulty
        if difficulty == "hard":
            answer_chance = 3
            timer = 10
            time_start = time.time()
        elif difficulty == "moderate":
            answer_chance = 3
        else:
            answer_chance = 100

        while answer_chance > 0 and (difficulty in ["easy", "moderate"] or (difficulty == "hard" and timer > 0)):
            if difficulty == "hard":
                #prints the value of timer (it's 10) and gets answer
                answer = simpledialog.askstring("Input", f"What is the answer to: {equation}?-----Time remaining: {timer:.1f} seconds")
            else:
                #gets answer(easy, moderate difficulties)
                answer = simpledialog.askstring("Input", f"What is the answer to: {equation}?")

            #when cancel is clicked, it goes to the next question
                if answer is None:
                    break
                        
            try:
                #evaluate/solve the equation/math problem
                result = eval(equation)
                #round the answer to two(2) decimal point if applicable
                rounded_result = round(result, 2)
                # Convert the user's answer to a float
                converted_answer = float(answer)
                # Compare the user's answer to the correct answer
                if converted_answer == rounded_result:
                    messagebox.showinfo("Math Mastermind", "Correct!")
                    #increment the correct answer
                    correct_answer += 1
                    break
                else:
                    messagebox.showinfo("Math Mastermind", "Incorrect!")
                    #decrement the chance of answering
                    answer_chance -= 1
            #if the user didn't enter a number
            except ValueError:
                messagebox.showerror("Math Mastermind", "!!!Error!!! \n Invalid input. Please enter a numeric value.")

                if difficulty == "hard":
                    #calculate the remaining time since the 10 seconds starts
                    time_remaining = timer - (time.time() - time_start)
                    #checks the time
                    if time_remaining <= 0:
                        messagebox.showinfo("Math Mastermind", "Out of time!")
                        break
                    #updates the time remaining variable
                    timer = time_remaining
            #decrements the math problems
        num_problems -= 1

    # Display the score
    messagebox.showinfo("Game Over", f"Your final score is {correct_answer} / {score}")

    # Ask if the user wants to play again
    play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
    if play_again:
        root.deiconify()
        difficulty_var.set("easy")
        equation_var.set("add")
        num_problems_entry.delete(0, tk.END)
    else:
        # Close the application
        root.destroy()

#makes equation ex. 1 + 1 and generate numbers according to difficulty
def make_equation(difficulty, equation_type):
    operator = operator_type[equation_type]

    if difficulty == "easy":
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
    elif difficulty == "moderate":
        num1 = random.randint(11, 100)
        num2 = random.randint(11, 100)
    elif difficulty == "hard":
        num1 = random.randint(101, 1000)
        num2 = random.randint(101, 1000)
    else:
        raise ValueError("Invalid Difficulty Level.")

    equation = f"{num1} {operator} {num2} "
    return equation

# Run the tkinter GUI as the game
root.mainloop()
