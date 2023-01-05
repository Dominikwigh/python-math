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
    print("Which would you like to play?")
    print("A - addition")
    print("B - multiplication")
    print("C - subtraction")
    print("D - Exit Game")
    
    choice = input("> ")

    if choice == "A":
        operator.add
    elif choice == "B":
        operator.mul
    elif choice == "C":
        operator.sub
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


def addition():
    
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    print(f'What is {num1} + {num2}?')
    
    choice = input("> ")
    if int(choice) == num1 + num2:
        print("Correct!")

    else: 
        print("Incorrect!")
addition()




