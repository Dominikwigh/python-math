import random 
import operator 


def display_intro():
    """
    display a title for the the game
    """
    title = "** A Simple Math Test **"
    print("*" * len(title))
    print(title)
    print("*" * len(title))

display_intro()

name = input("Enter Yout Name To Start The Game: ")
print("Hello " + name + "! " + "Good Luck" + "!")
