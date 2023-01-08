import random
import operator
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
    print("Hello " + name + "! ")


display_intro()


def start_game():
    """
    This function creates the game choices
    """
    print("Which would you like to play?")
    list = ["1 - Addition", "2 - Multiplication", "3 - Subtraction", 
    "4 - Exit"]
    print(list[0])
    print(list[1])
    print(list[2])
    print(list[3])

    choice = input("> ")

    if choice == "1":
        addition()
    elif choice == "2":
        multiplication()
    elif choice == "3":
        subtraction()
    elif choice == "4":
        return display_intro()
    try:
        print("Invalid menu option!")
        start_game()
    except ValueError:
        print("That was not a number")


def addition(): 
    """
    addition part of game with timer
    """

    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    start_time = time()
    print(f'What is {num1} + {num2}?')
    user_choice = int(input("> "))
    elapsed_time = time() - start_time
    if int(user_choice) == num1 + num2:
        print(f'Correct, in {elapsed_time:.2f} seconds')
        start_game()
    else:
        print("Incorrect!")
        start_game()


def multiplication():
    """
    multiplication part of game with timer
    """

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    start_time = time()
    print(f'What is {num1} x {num2}?')

    user_choice = int(input("> "))
    elapsed_time = time() - start_time
    if int(user_choice) == num1*num2:
        print(f'Correct, in {elapsed_time:.2f} seconds')
        start_game()
    else:
        print("Incorrect!")
        start_game()


def subtraction():

    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    print(f'What is {num1} - {num2}?')

    user_choice = int(input("> "))
    if int(user_choice) == num1 - num2:
        print("Correct!")
        start_game()

    else:
        print("Incorrect!") 
        start_game()


def display_result(total, score, user_choice):
    if total > 0:
        user_choice = score / total
        print("You answerd", total, "questions with", score)


def game(score):
    option = start_game()
    total = 0
    score = 0
    while option != 4:
        total += 1


start_game()
