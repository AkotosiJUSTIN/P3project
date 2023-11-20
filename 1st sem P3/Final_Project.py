import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import time

#dictionary of operator type
operator_type = {"add": "+", "subtract": "-", "multiply": "*", "divide": "/"}

#GUI
class MathGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Math Mastermind")
        #text on top of the drawer
        self.difficulty_label = tk.Label(master, text="Choose a difficulty level:")
        self.difficulty_label.pack()
        #drawer of difficulties
        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set("easy")
        self.difficulty_menu = tk.OptionMenu(master, self.difficulty_var, "easy", "moderate", "hard")
        self.difficulty_menu.pack()
        #text on top of the drawer
        self.equation_label = tk.Label(master, text="Choose an equation type:")
        self.equation_label.pack()
        #drawer of equations
        self.equation_var = tk.StringVar()
        self.equation_var.set("add")
        self.equation_menu = tk.OptionMenu(master, self.equation_var, "add", "subtract", "multiply", "divide")
        self.equation_menu.pack()
        #text on top of the drawer
        self.num_problems_label = tk.Label(master, text="Enter the number of problems:")
        self.num_problems_label.pack()
        #box that user can put their answer about how many problems they want to answer
        self.num_problems_entry = tk.Entry(master)
        self.num_problems_entry.pack()
        #button to start the game
        self.play_button = tk.Button(master, text="Play Game", command=self.start_game)
        self.play_button.pack()

    def start_game(self):
        difficulty = self.difficulty_var.get()
        equation_type = self.equation_var.get()

        try:
            score = int(self.num_problems_entry.get())
            if score <= 0:
                messagebox.showerror("Math Mastermind", "!!!Error!!! \n Please enter a positive number.")
                return
        except ValueError:
            messagebox.showerror("Math Mastermind", "!!!Error!!! \n Invalid input. Please enter a valid number.")
            return
        # Hide the main window
        self.master.withdraw()  
        self.play_game(difficulty, equation_type, score)

    def play_game(self, difficulty, equation_type, score):
        num_problems = score
        correct_answer = 0

        while num_problems > 0:
            equation = self.make_equation(difficulty, equation_type)

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
                    answer = simpledialog.askstring("Math Mastermind", f"What is the answer to: {equation}?-----Time remaining: {timer:.1f} seconds")
                else:
                    #gets answer(easy, moderate difficulties)
                    answer = simpledialog.askstring("Math Mastermind", f"What is the answer to: {equation}?")
                    
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
        messagebox.showinfo("Math Mastermind", f"!!!Game Over!!! \n Your final score is {correct_answer} / {score}")

        # Ask if the user wants to play again
        play_again = messagebox.askyesno("Math Mastermind", "???Play Again??? \n Do you want to play again?")
        if play_again:
            self.master.deiconify()  # Show the main window again
            self.difficulty_var.set("easy")
            self.equation_var.set("add")
            self.num_problems_entry.delete(0, tk.END)
        else:
            self.master.destroy()  # Close the application
    #makes equation ex. 1 + 1 and generate numbers according to difficulty
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

# Create the main tkinter gui game window
root = tk.Tk()

# Create an instance of the GameGUI class
math_game_gui = MathGameGUI(root)

# Run the tkinter gui as game
root.mainloop()
