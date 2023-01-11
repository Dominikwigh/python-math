import random
from time import time


def display_intro():
    """
    displaying a title to the the game
    """
    title = "** Welcome To Math Practice! **"
    print("*" * len(title))
    print(title)
    print("*" * len(title))
    name = input("Enter Your Name To Start The Game: ")
    print("**** Hello " + name + "! ****")
    print("-----------------")


display_intro()


def validate_data():
    """
    A function to validate the data that is put in as an answer
    """
    while True:
        choice = input("> ")
        try:
            int(choice)
            break
        except ValueError:
            print("Value must be an integer")
    return choice


def start_game():
    """
    This function creates the game choices
    """
    print("Which would you like to play?")
    print("-----------------")
    menu_list = ["1-Addition", "2-Multiplication", "3-Subtraction", "4-Exit"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])
    print(menu_list[3])

    choice = input("> ")

    if choice == "1":
        addition()
    elif choice == "2":
        multiplication()
    elif choice == "3":
        subtraction()
    elif choice == "4":
        exit_game()
    else:
        print("-----------------")
        print("Number has to be between 1-4")
        display_intro()
        start_game()


def addition():
    """
    addition part of game with timer
    """
    num1 = random.randint(1, 20)
    num2 = random.randint(5, 25)
    start_time = time()
    print(f'What is {num1} + {num2}?')
    choice = validate_data()
    elapsed_time = time() - start_time
    if int(choice) == num1 + num2:
        print(f'Correct, in {elapsed_time:.2f} seconds')
    else:
        print("Incorrect")


def multiplication():
    """
    multiplication part of game with timer
    """
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    start_time = time()
    print(f'What is {num1} x {num2}?')
    choice = validate_data()
    elapsed_time = time() - start_time
    if int(choice) == num1 * num2:
        print(f'Correct, in {elapsed_time:.2f} seconds')
    else:
        print("Incorrect!")


def subtraction():
    """
    subtraction part of game with timer
    """
    num1 = random.randint(0, 20)
    num2 = random.randint(0, 20)
    start_time = time()
    print(f'What is {num1} - {num2}?')

    choice = validate_data()
    elapsed_time = time() - start_time
    if int(choice) == num1 - num2:
        print(f'Correct, in {elapsed_time:.2f} seconds')
    else:
        print("Incorrect!")


def exit_game():
    """
    function to exit game
    """
    print("You just left the game!")


start_game()
