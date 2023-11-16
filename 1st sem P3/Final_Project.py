import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import time

operator_type = {"add": "+", "subtract": "-", "multiply": "*", "divide": "/"}

class MathGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Math Mastermind")

        self.difficulty_label = tk.Label(master, text="Choose a difficulty level:")
        self.difficulty_label.pack()

        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set("easy")
        self.difficulty_menu = tk.OptionMenu(master, self.difficulty_var, "easy", "moderate", "hard")
        self.difficulty_menu.pack()

        self.equation_label = tk.Label(master, text="Choose an equation type:")
        self.equation_label.pack()

        self.equation_var = tk.StringVar()
        self.equation_var.set("add")
        self.equation_menu = tk.OptionMenu(master, self.equation_var, "add", "subtract", "multiply", "divide")
        self.equation_menu.pack()

        self.num_problems_label = tk.Label(master, text="Enter the number of problems:")
        self.num_problems_label.pack()

        self.num_problems_entry = tk.Entry(master)
        self.num_problems_entry.pack()

        self.play_button = tk.Button(master, text="Play Game", command=self.start_game)
        self.play_button.pack()

    def start_game(self):
        difficulty = self.difficulty_var.get()
        equation_type = self.equation_var.get()

        try:
            desired_score = int(self.num_problems_entry.get())
            if desired_score <= 0:
                messagebox.showerror("Error", "Please enter a positive number.")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")
            return

        self.master.withdraw()  # Hide the main window
        self.play_game(difficulty, equation_type, desired_score)

    def play_game(self, difficulty, equation_type, desired_score):
        num_problems = desired_score
        correct_answer = 0

        while num_problems > 0:
            equation = self.make_equation(difficulty, equation_type)

            if difficulty == "easy":
                answer_limit = 1
            else:
                answer_limit = 3

            if difficulty == "hard":
                timer = 10
                start_time = time.time()

            while answer_limit > 0 and (difficulty in ["easy", "moderate"] or (difficulty == "hard" and timer > 0)):
                if difficulty == "hard":
                    print(f"Time remaining: {timer:.1f} seconds")

                answer = simpledialog.askstring("Input", f"What is the answer to: {equation}?")

                try:
                    result = eval(equation)
                    rounded_result = round(result, 2)
                    converted_answer = float(answer)

                    if converted_answer == rounded_result:
                        messagebox.showinfo("Result", "Correct!")
                        correct_answer += 1
                        break
                    else:
                        messagebox.showinfo("Result", "Incorrect!")
                        answer_limit -= 1

                except ValueError:
                    messagebox.showerror("Error", "Invalid input. Please enter a numeric value.")

                if difficulty == "hard":
                    remaining_time = timer - (time.time() - start_time)

                    if remaining_time <= 0:
                        messagebox.showinfo("Time Out", "Out of time!")
                        break

                    timer = remaining_time

            num_problems -= 1

        # Display the final score
        messagebox.showinfo("Game Over", f"Your final score is {correct_answer} / {desired_score}")

        # Ask if the user wants to play again
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            self.master.deiconify()  # Show the main window again
            self.difficulty_var.set("easy")
            self.equation_var.set("add")
            self.num_problems_entry.delete(0, tk.END)
        else:
            self.master.destroy()  # Close the application

    def make_equation(self, difficulty, equation_type):
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

# Create the main Tkinter window
root = tk.Tk()

# Create an instance of the MathGameGUI class
math_game_gui = MathGameGUI(root)

# Run the Tkinter event loop
root.mainloop()
