import tkinter as tk
from tkinter import messagebox
import random
import time

# Create a map to convert equation type to operator.
equation_type_to_operator_map = {
    "add": "+",
    "subtract": "-",
    "multiply": "*",
    "divide": "/"
}

# Get the valid difficulty level from the user.
def get_valid_difficulty():
    while True:
        difficulty = input("Choose a difficulty level (easy, moderate, or hard): ")
        if difficulty in ["easy", "moderate", "hard"]:
            return difficulty
        else:
            print("Invalid input. Try again.")

# Generate a random math equation based on the difficulty and equation type.
def generate_math_equation(difficulty: str, equation_type: str) -> str:
    operator = equation_type_to_operator_map[equation_type]

    if difficulty == "easy":
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
    elif difficulty == "moderate":
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
    else:
        num1 = random.randint(100, 999)
        num2 = random.randint(100, 999)

    return f"{num1} {operator} {num2}"

# Convert the math equation to a string format for display.
def convert_math_equation_to_string(equation: str) -> str:
    operator = equation_type_to_operator_map[equation_type]
    return equation.replace(operator, f" {operator} ")

# Define the main game class.
class MathGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Math Game")
        self.geometry("400x400")

        self.equation_type = tk.StringVar()
        self.equation_type.set("add")

        self.difficulty = tk.StringVar()
        self.difficulty.set("easy")

        self.equation = None

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Choose a difficulty level:").pack()
        tk.Radiobutton(self, text="Easy", variable=self.difficulty, value="easy").pack()
        tk.Radiobutton(self, text="Moderate", variable=self.difficulty, value="moderate").pack()
        tk.Radiobutton(self, text="Hard", variable=self.difficulty, value="hard").pack()

        tk.Label(self, text="Choose an equation type:").pack()
        tk.Radiobutton(self, text="Add", variable=self.equation_type, value="add").pack()
        tk.Radiobutton(self, text="Subtract", variable=self.equation_type, value="subtract").pack()
        tk.Radiobutton(self, text="Multiply", variable=self.equation_type, value="multiply").pack()
        tk.Radiobutton(self, text="Divide", variable=self.equation_type, value="divide").pack()

        tk.Button(self, text="Generate and Display Equation", command=self.generate_and_display_equation).pack()
        tk.Label(self, text="").pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        tk.Button(self, text="Check Answer", command=self.check_answer).pack()

    def generate_and_display_equation(self):
        self.equation = generate_math_equation(self.difficulty.get(), self.equation_type.get())
        tk.Label(self, text=f"Solve the equation: {convert_math_equation_to_string(self.equation)}").pack()

    def check_answer(self):
        answer = self.entry.get()
        self.entry.delete(0, tk.END)

        if not answer:
            messagebox.showerror("Error", "No answer entered. Try again.")
            return

        correct_answer = eval(self.equation)

        if str(correct_answer) == answer:
            messagebox.showinfo("Correct", "You got it right!")
        else:
            messagebox.showerror("Incorrect", f"Sorry, the correct answer is {correct_answer}.")

if __name__ == "__main__":
    game = MathGame()
    game.mainloop()