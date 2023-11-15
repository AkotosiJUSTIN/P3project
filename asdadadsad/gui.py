import tkinter as tk
from tkinter import messagebox, simpledialog  
import random
import time

equation_type_to_operator_map = {
    "add": "+",
    "subtract": "-",
    "multiply": "*",
    "divide": "/",
}

class MathGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Math Game")

        self.welcome_label = tk.Label(master, text="Welcome to the math game!")
        self.welcome_label.pack()

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

        self.start_button = tk.Button(master, text="Start Game", command=self.start_game)
        self.start_button.pack()

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
        correct_answers = 0

        while num_problems > 0:
            equation = self.generate_math_equation(difficulty, equation_type)

            if difficulty == "easy":
                answer_limit = 1
            else:
                answer_limit = 3

            if difficulty == "hard":
                timer = 10
                start_time = time.time()

            while answer_limit > 0 and (difficulty in ["easy", "moderate"] or (difficulty == "hard" and timer > 0)):
                if difficulty == "hard":
                    print(f"Time remaining: {timer:.2f} seconds")

                answer = simpledialog.askstring("Input", f"What is the answer to: {equation}?")

                try:
                    evaluated_equation = eval(equation)
                    evaluated_answer = eval(answer)

                    if evaluated_equation == evaluated_answer:
                        messagebox.showinfo("Result", "CORRECT!!")
                        correct_answers += 1
                        break
                    elif evaluated_equation != evaluated_answer:
                        messagebox.showinfo("Result", "INCORRECT!!")
                        answer_limit -= 1

                except Exception as e:
                    messagebox.showerror("Error", f"Invalid input. {str(e)}")

                if difficulty == "hard":
                    remaining_time = timer - (time.time() - start_time)

                    if remaining_time <= 0:
                        messagebox.showinfo("Time Out", "Out of time!")
                        break

                    timer = remaining_time
            num_problems -= 1

        # Display the score after completing all the problems.
        messagebox.showinfo("Game Over", f"Your final score is {correct_answers} / {desired_score}")

        # Ask if the user wants to play again
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            self.master.deiconify()  # Show the main window again
            self.difficulty_var.set("easy")
            self.equation_var.set("add")
            self.num_problems_entry.delete(0, tk.END)
        else:
            self.master.destroy()  # Close the application

    def generate_math_equation(self, difficulty: str, equation_type: str) -> str:
        operator = equation_type_to_operator_map[equation_type]

        if difficulty == "easy":
            num1 = random.randint(0, 9)
            num2 = random.randint(0, 9)
        elif difficulty == "moderate":
            num1 = random.randint(10, 99)
            num2 = random.randint(10, 99)
        elif difficulty == "hard":
            num1 = random.randint(100, 499)
            num2 = random.randint(100, 499)
        else:
            raise ValueError("Invalid difficulty level.")

        equation = f"{num1} {operator} {num2}"
        return equation

# Create the main Tkinter window
root = tk.Tk()

# Create an instance of the MathGameGUI class
math_game_gui = MathGameGUI(root)

# Run the Tkinter event loop
root.mainloop()
