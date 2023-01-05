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
        addition()
    elif choice == "B":
        multiplication()
    elif choice == "C":
        subtraction()
    elif choice == "D":
        return None
    else:
        print("That's not an option")
        start_game()


start_game()


def random_question():
    """
    a dictionary with operators
    """
    operators = {
        "A": operator.add,
        "B": operator.mul,
        "C": operator.sub,
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


addition()


def multiplication():

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    print(f'What is {num1} x {num2}?')

    choice = input("> ")
    if int(choice) == num1*num2:
        print("Correct!")

    else:
        print("Incorrect!")
        start_game()


multiplication()


def subtraction():

    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    print(f'What is {num1} - {num2}?')

    choice = input("> ")
    if int(choice) == num1 - num2:
        print("Correct!")

    else:
        print("Incorrect!")
        start_game()


subtraction()

###
def game():
    score = 0
    for i in range(5):
        if True:
            score += 1
    print(f'Your score is{score}')


game()
