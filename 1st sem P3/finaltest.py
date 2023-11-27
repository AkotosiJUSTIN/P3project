import tkinter as tk
from tkinter import messagebox, simpledialog
import sys
import random

operator_type = {"add": "+", "subtract": "-", "multiply": "*", "divide": "/"}

root = tk.Tk()
root.title("Math Mastermind")
root.geometry("600x500")
root['bg'] = '#5ba56e'

title = tk.Label(root, text="Math Mastermind", fg='black', height='3', font=("Arial", 40))
title['bg'] = '#5ba56e'
title.pack()

def show_information():
    information_text = ("Welcome to Math Mastermind!\n\n"
                        "Choose a difficulty level and an equation type.\n"
                        "Enter the number of problems you want to solve.\n"
                        "Click 'Play Game' to start the game.\n\n"
                        "For each problem, enter the correct answer within the given chances.\n"
                        "Cancel the game at any time by clicking the 'Cancel' button.\n\n"
                        "Good luck!")

    messagebox.showinfo("Math Mastermind Information", information_text)

i = 15
j = 550
info_button = tk.Button(root, text="?", command=show_information)
info_button['bg'] = '#5ba56e'
info_button.pack()
info_button.config(font=("Arial", 20), border=0, bg="#36c2f3", activebackground="#5ba56e")
info_button.place(y=i, x=j)

difficulty_label = tk.Label(root, text="Choose a difficulty level:", fg='black', font=("Arial", 20))
difficulty_label['bg'] = '#5ba56e'
difficulty_label.pack()

difficulty_var = tk.StringVar()
difficulty_var.set("easy")
difficulty_menu = tk.OptionMenu(root, difficulty_var, "easy", "moderate", "hard")
difficulty_menu.pack()
difficulty_menu.config(font=("Arial", 20), border=0, indicator=0, bg="#36c2f3", activebackground="#5ba56e")

equation_label = tk.Label(root, text="Choose an equation type:", fg='black', font=("Arial", 20))
equation_label['bg'] = '#5ba56e'
equation_label.pack()

equation_var = tk.StringVar()
equation_var.set("add")
equation_menu = tk.OptionMenu(root, equation_var, "add", "subtract", "multiply", "divide")
equation_menu.pack()
equation_menu.config(font=("Arial", 20), border=0, indicator=0, bg="#36c2f3", activebackground="#5ba56e")

num_problems_label = tk.Label(root, text="Enter the number of problems:", fg='black', font=("Arial", 20))
num_problems_label['bg'] = '#5ba56e'
num_problems_label.pack()

num_problems_entry = tk.Entry(root)
num_problems_entry.pack()
num_problems_entry.config(font=("Arial", 20), border=0)


def start_game():
    difficulty = difficulty_var.get()
    equation_type = equation_var.get()

    score = 0  # Initialize score at a higher level

    try:
        score = int(num_problems_entry.get())
        if score <= 0:
            messagebox.showerror("Error", "Please enter a positive number.")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
        return

    root.withdraw()
    play_game(difficulty, equation_type, score, 0)

play_button = tk.Button(root, text="Play Game", command=start_game)
play_button['bg'] = '#5ba56e'
play_button.pack()
play_button.config(font=("Arial", 20), border=0, bg="#36c2f3")

def play_game(difficulty, equation_type, num_problems, correct_answer, score):
    while num_problems > 0:
        equation, result = make_equation(difficulty, equation_type)

        if difficulty == "hard":
            answer_chance = 1
        elif difficulty == "moderate":
            answer_chance = 3
        else:
            answer_chance = 10

        # Check if the root window still exists
        if not root.winfo_exists():
            break

        while answer_chance > 0:
            answer_window = tk.Toplevel(root)
            answer_window.title("Math Mastermind")
            answer_window.geometry("400x200")

            equation_label = tk.Label(answer_window, text=f"Equation: {equation}", font=("Arial", 16))
            equation_label.pack()

            answer_entry = tk.Entry(answer_window)
            answer_entry.pack()

            submit_button = tk.Button(answer_window, text="Submit", command=lambda: check_answer(answer_window, equation, answer_entry, correct_answer, num_problems, difficulty, equation_type, result))
            submit_button.pack()

            answer_window.wait_window()

        num_problems -= 1

    # Ask if the user wants to play again
    if root.winfo_exists():
        game_over_message = f"Game Over! Your score: {correct_answer}/{score}\n\nDo you want to play again?"
        play_again = messagebox.askyesno("Math Mastermind", game_over_message)

        if play_again:
            root.deiconify()
            difficulty_var.set("easy")
            equation_var.set("add")
            num_problems_entry.delete(0, tk.END)
        else:
            # Close the application
            root.destroy()



def handle_close_button(answer_window):
    # Handle the close button by destroying the window without affecting the game state
    answer_window.destroy()

def check_answer(answer_window, equation, answer_entry, correct_answer, num_problems, difficulty, equation_type, result):
    answer = answer_entry.get()

    if answer:
        try:
            converted_answer = float(answer)

            if converted_answer == result:
                messagebox.showinfo("Math Mastermind", "Correct!")
                correct_answer += 1
                answer_window.destroy()
                num_problems -= 1
                play_game(difficulty, equation_type, num_problems, correct_answer)
            else:
                messagebox.showinfo("Math Mastermind", "Incorrect!")
        except ValueError:
            messagebox.showerror("Math Mastermind", "!!!Error!!! \n Invalid input. Please enter a numeric value.")
        finally:
            answer_window.destroy()
def make_equation(difficulty, equation_type):
    operator = operator_type[equation_type]

    if difficulty == "easy":
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
    elif difficulty == "moderate":
        num1 = random.randint(101, 1000)
        num2 = random.randint(101, 1000)
    elif difficulty == "hard":
        num1 = random.randint(1001, 5000)
        num2 = random.randint(1001, 5000)
    else:
        raise ValueError("Invalid Difficulty Level.")

    equation = f"{num1} {operator} {num2}"
    result = eval(equation)
    return equation, result

root.mainloop()
