import random
import operator


def display_intro():
    """
    displaying a title to the the game
    """
    title = "** Welcome To Math Practice! **"
    print("*" * len(title))
    print(title)
    print("*" * len(title))
    name = input("Enter Your Name To Start The Game: ")
    print("Hello " + name + "! ")


display_intro()


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
        addition()
    elif choice == "B":
        multiplication()
    elif choice == "C":
        subtraction()
    elif choice == "D":
        return start_game()
    else:
        print("That's not an option")
        start_game()




def question():
    """
    a dictionary with operators
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
        start_game()


def multiplication():

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    print(f'What is {num1} x {num2}?')

    choice = input("> ")
    if int(choice) == num1*num2:
        print("Correct!")
        start_game()

    else:
        print("Incorrect!")
        start_game()


def subtraction():

    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    print(f'What is {num1} - {num2}?')

    choice = input("> ")
    if int(choice) == num1 - num2:
        print("Correct!")

    else:
        print("Incorrect!") 


def display_score():
    score = 0
    for i in range(3):
        if True:
            score += 1
            print(f'Your score is {score}')


start_game()
