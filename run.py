import random 
import operator 


def display_intro():
    """
    display a title for the the game
    """
    title = "** Welcome To Math Practice! **"
    print("*" * len(title))
    print(title)
    print("*" * len(title))


display_intro()

name = input("Enter Yout Name To Start The Game: ")
print("Hello " + name + "! " + "Good Luck" + "!")

def start_game():
    """
    This function creates the game choices
    """
    print("Wgich would you like to play?")
    print("A - Addition")
    print("B - Multiplication")
    print("C - Subtraction")
    print("D - Exit Game")


start_game()


def random_question():
    """
    a dictionary with operators and function to randomly
     select the number on the right and left 
    """
    operators = {
        "+": operator.add,
        "*": operator.mul,
        "-": operator.sub,
        "%": operator.mod
    }

# random numbers between 1 - 25 
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(num1, num2)
    print(f'What is {num1} {operation} {num2}?')
    return answer


def user_answer():
    """
    A function to get the users input 
    """
    answer = random_question()
    guess = float(input())
    return guess == answer


def start_game():
    """
    A function to start the game and loop through questions 
    and increment score 
    """
