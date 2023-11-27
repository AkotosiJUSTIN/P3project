import tkinter as tk
from tkinter import messagebox, simpledialog
import sys
import random

# Dictionary of operator type
operator_type = {"add": "+", "subtract": "-", "multiply": "*", "divide": "/"}

# GUI initialization
root = tk.Tk()
root.title("Math Mastermind")
root.geometry("600x500")
root['bg']='#add8e6'

#title
title = tk.Label(root, text="Math Mastermind",fg='#000080', height='1', font=("helvetica",40))
title['bg']='#add8e6'
title.pack(pady=40,)

#show information
def show_information():
    information_text = ("Welcome to Math Mastermind!\n\n"
                        "Choose a difficulty level and an equation type.\n"
                        "Enter the number of problems you want to solve.\n"
                        "Click 'Play Game' to start the game.\n\n"
                        "For each problem, enter the correct answer within the given chances.\n"
                        "Cancel the game at any time by clicking the 'Cancel' button.\n\n"
                        "Good luck!\n"
                        "HEHE    XD")
    
    messagebox.showinfo("Math Mastermind Information", information_text)
#?/info button
i=15
j=550
info_button = tk.Button(root, text="?", command=show_information)
info_button['bg']='#000080'
info_button.pack()
info_button.config(font=("helvetica",20), border=2, bg="#add8e6", activebackground="#90ee90")
info_button.place(y=i, x=j)

#text on top of the drawer
difficulty_label = tk.Label(root, text="Choose a difficulty level:", fg='#000080', font=("helvetica",20))
difficulty_label['bg']='#add8e6'
difficulty_label.pack()

#drawer of difficulties
difficulty_var = tk.StringVar()
difficulty_var.set("easy")
difficulty_menu = tk.OptionMenu(root, difficulty_var, "easy", "moderate", "hard")
difficulty_menu.pack()
difficulty_menu.config(font=("helvetica",20), border=2, indicator=0, bg="#add8e6", activebackground="#90ee90",  fg='#000080')

#text on top of the drawer
equation_label = tk.Label(root, text="Choose an equation type:", fg='#000080', font=("helvetica",20))
equation_label['bg']='#add8e6'
equation_label.pack()

#drawer of equations
equation_var = tk.StringVar()
equation_var.set("add")
equation_menu = tk.OptionMenu(root, equation_var, "add", "subtract", "multiply", "divide")
equation_menu.pack()
equation_menu.config(font=("helvetica",20), border=2, indicator=0, bg="#add8e6", activebackground="#90ee90",  fg='#000080')

#text on top of the drawer
num_problems_label = tk.Label(root, text="Enter the number of problems:",  fg='#000080', font=("helvetica",20))
num_problems_label['bg']='#add8e6'
num_problems_label.pack()

#box that user can put their answer about how many problems they want to answer
num_problems_entry = tk.Entry(root, justify='center')
num_problems_entry.pack()
num_problems_entry.config(font=("helvetica",20), border=5,  fg='#000080')

# Button to start the game
def start_game():
    difficulty = difficulty_var.get()
    equation_type = equation_var.get()

    try:
        score = int(num_problems_entry.get())
        if score <= 0:
            #if the user put 0 or negative numbers
            messagebox.showerror("Math Mastermind", "                           Error!!                             \n \n          Please enter a positive number.          ")
            return
    except ValueError:
        #if the user didn't put number
        messagebox.showerror("Math Mastermind", "                         Error!!                           \n \n                     Invalid input.                     \n \n           Please enter a valid number.          ")
        return

    # Hide the main window
    root.withdraw()
    play_game(difficulty, equation_type, score)

#button for play
play_button = tk.Button(root, text="Play Game", command=start_game)
play_button['bg']='#000080'
play_button.pack()
play_button.config(font=("helvetica",20), border=2, bg="#add8e6", activebackground="#90ee90")

def play_game(difficulty, equation_type, score):


    
    num_problems = score
    #counter of correct answer
    correct_answer = 0
    
    #lops until there's no problems
    while num_problems > 0:
        equation = make_equation(difficulty, equation_type)\

        #limit answers 
        if difficulty == "hard":
            answer_chance = 1
        elif difficulty == "moderate":
            answer_chance = 3
        else:
            answer_chance = 10

        while answer_chance > 0:
            #gets answer(easy, moderate difficulties) and print the equation/problems
            answer = simpledialog.askstring("Math Mastermind", f"          What is the answer to: {equation}?           \n \n                Chances remaining: {answer_chance}                \n \n                          Score:{correct_answer} / {score}                        ")
            
            #if cancel button is used, the game will break
            if answer is None:
                messagebox.showinfo("Math Mastermind", "                   Game Over!!               \n \n           Game canceled by user.          ")
                root.destroy()
                sys.exit(0)
                
            
            try:
                #evaluate/solve the equation/math problem
                result = eval(equation)
                #round the answer to two(2) decimal point if applicable
                rounded_result = round(result, 2)
                # Convert the user's answer to a float
                converted_answer = float(answer)
                # Compare the user's answer to the correct answer
                if converted_answer == rounded_result:
                    messagebox.showinfo("Math Mastermind", "          Correct!!           ")
                    #increment the correct answer
                    correct_answer += 1
                    break
                else:
                    messagebox.showinfo("Math Mastermind", "         Incorrect!!          ")
                    #decrement the chance of answering
                    answer_chance -= 1
            #if the user didn't enter a number
            except ValueError:
                messagebox.showerror("Math Mastermind", "                           Error!!                      \n \n                     Invalid input.                    \n \n           Please enter a numeric value.          ")
        #decrements the math problems
        num_problems -= 1

    # Display the score
    messagebox.showinfo("Math Mastermind", f"                    Game Over          \n \n          Your final score is: {correct_answer} / {score}          ")

    # Ask if the user wants to play again
    play_again = messagebox.askyesno("Math Mastermind", "                    Play Again??          \n \n          Do you want to play again?          ")
    if play_again:
        #returns to the main window
        root.deiconify()
        difficulty_var.set("easy")
        equation_var.set("add")
        #resets the num problem
        num_problems_entry.delete(0, tk.END)
    else:
        # Close the application
        root.destroy()

#makes equation ex. 1 + 1 and generate numbers according to difficulty
def make_equation(difficulty, equation_type):
    operator = operator_type[equation_type]
    
    #generates random numbers
    if difficulty == "easy":
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
    elif difficulty == "moderate":
        num1 = random.randint(101, 1000)
        num2 = random.randint(101, 1000)
    else:
        num1 = random.randint(1001, 5000)
        num2 = random.randint(1001, 5000)

    equation = f"{num1} {operator} {num2} "
    return equation

# Run the tkinter GUI as the game
root.mainloop()