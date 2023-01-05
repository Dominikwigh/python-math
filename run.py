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
print("Hello " + name + "! ")


def start_game():
    """
    This function creates the game choices
    """
    print("Wgich would you like to play?")
    print("A - addition")
    print("B - multiplication")
    print("C - subtraction")
    print("D - Exit Game")
    
    choice = input("> ")

    if choice == "A":
        addition()
    elif choice == "B":
        multiplication()
    elif choice == "c":
        subtraction()
    elif choice == "D":
        return None
    else: 
        print("That's not a function")
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



