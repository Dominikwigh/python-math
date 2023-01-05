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


