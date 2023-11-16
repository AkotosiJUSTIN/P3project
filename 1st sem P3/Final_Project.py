import random
import time

#dictionary of operator type
operator_type = { "add": "+", "subtract": "-", "multiply": "*", "divide": "/",}

#input/get of difficulty
def get_difficulty():
    while True:
        difficulty = input("Choose a difficulty level(easy/moderate/hard)")
        if difficulty in ["easy", "Moderate", "hard"]:
            return difficulty
        else:
            print("Invalid Input. Try Again.")

#input/get of equation
def get_equation():
    while True:
        equation_type = input("Choose an equation type (add/subtract/multiply/divide): ")
        if equation_type in ["add", "subtract", "multiply", "divide"]:
            return equation_type
        else:
            print("Invalid Input. Try Again.")

#input/get of number of problems
def get_num_problems():
    while True:
        try:
            score = int(input("How many problems do you want to solve? "))
            if score > 0:
                return score
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid Input. Please Enter A Number.")

#makes equation ex. 1 + 1 and generate numbers according to difficulty
def make_equation(difficulty, equation_type):
    operator = operator_type[equation_type]
    
    if difficulty == "easy":
        num1 = random.randint(0,10)
        num2 = random.randint(0,10)
    elif difficulty == "moderate":
        num1 = random.randint(11,100)
        num2 = random.randint(11,100)
    elif difficulty == "hard":
        num1 = random.randint(101,1000)
        num2 = random.randint(101,1000)
    else:
        raise ValueError("Invalid Difficulty Level.")
    
    equation = f"{num1} {operator} {num2} "
    return equation

#play math game
def play(difficulty, equation_type, score):
    #number to of problems to solve
    num_problems = score
    #numbers of correct answers solved
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
        
        #print math problem
        print(equation)
        
        while answer_chance > 0 and (difficulty in ["easy", "moderate"] or (difficulty == "hard" and timer > 0)):
            if difficulty == "hard":
                #prints the value of timer (it's 10)
                print(f"Time remaining: {timer:.1f} seconds")
            
            #gets answer
            answer = input("What is the answer?")
            #evaluate/solve the equation/math problem
            result = eval(equation)
            #round off the answer to 2 decimal point
            rounded_result = round(result, 2)
            
            try:
                # Convert the user's answer to a float
                converted_answer = float(answer)

                # Compare the user's answer to the correct answer
                if converted_answer == rounded_result:
                    print("Correct!!!")
                    #increment the correct answer
                    correct_answer +=1
                    break
                else:
                    print("Incorrect!!!")
                    #decrement the chance of answering
                    answer_chance -=1
            #if the user didn't enter a number
            except ValueError:
                    print("Invalid input. Please enter a numeric value.")   

            if difficulty == "hard":
                #calculate the remaining time since the 10 seconds starts
                time_remaining = timer - (time.time() - time_start)
                
                #check if the time
                if time_remaining <= 0:
                    print("Out Of Time!!!")
                    break
                #updates the time remaining variable
                timer = time_remaining
        #decrements the math problems
        num_problems -= 1
    
    #show score
    print(f"Your score is {correct_answer} / {score}")
    
    #ask if he wants to play again
    play_again = input("Do you want to play again? If yes, enter <y>: ")
    if play_again == "y":
        play(difficulty, equation_type, score)
        
# start game
print("Welcome to Math Mastermind!!!")

#get user difficulty   
difficulty = get_difficulty()

#get user equation
equation = get_equation()

#get user number of problems
score = get_num_problems()

#play game
play(difficulty, equation, score)