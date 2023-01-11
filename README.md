# Maths Game #
---
Maths game is a python terminal game, which has been devoloped using Gitpod and deployed on Heroku. 

Users have the chance to practice their math. They will be able to practice, "addition", "multiplication" and "subtraction". 
When completing a challange the user gets a answer if correct/ incorrect. 

folder/image.png
--- 
## Instructions on how to play ##

The maths game is a simple terminal game designed to test users knowledge. 
There are four options to choose from to play. 
At the start of the game you are presented by a title with the text of "Welcome to math practice". 
Below the title is a text of "Enter your name to start the game" for the user to enter their name and then start the game. 
on the next part the user is greeted and have the options to choose what to play. When the user has selected a game they then get a question and have to answer, either if its correct or incorrect the user gets the result after they have put in a answer. They are also provided with a time of how long it took them to answer the question, but only if they get it right. 
To play agin the user has to run the program.  

--- 
## Project Goals ##

This project was created for Code institutes full stack development course. 
* Main goals 
   * Create a terminal game using the Python language. 
   * Make the game easy to play but still challenging.
* User targets
   * Users that want to test their knowledge.

---
## Features ##
*  Start screen 
    * When the run button is clicked the user is presented with a start screen. 
    * A title is shown and a Enter your name text, where the user have to enter a name to start the game. 
folder/image.png

* Choose game
    * This next function will say "Hello 'user'", and then ask for the user to choose a game to play.
    * Addition, multiplication, subtraction or exit game. 

* Game selected 
    * This will, after choosing a game provide the user with a problem to solve, and if correct the user sees corrcet with a time that it took the user to answer. 
    * If the answer is incorrect it tells the user that. 

When the run program button is clicked at the top the game will restart. 

## Testing ## 
### Manual Testing ###
I have manually tested the program by doing this.. 
* Passed thorugh a PEP8 linter and confirmed that there are no problems. 
* Tested answers by inputting incorrcet values(string instead of integer, numbers higher than 4).
* Tested both on Gitpod and Heroku Terminal. 

### Validator testing ### 
folder/image.png

### Bug Testing 

### Unresolved bugs
No unresolved bugs where detected. 


## Deployment ##
---
The steps to deploy are as follows..
* Go to Heroku and at the top click on the "new" button to create a new app. 
* Enter a unique name and choose Europe as region and click create app. 
* Go to settings and select "config vars". 
* Add a new "config var" with the name of PORT and value 8000.
* Locate "Buildpacks" and add Python and node.js in this order, it should always be in this order. 
* Exit the settings and click Deploy and click Github from the deploy options. 
* Select your repository and connect it to Heroku. 
* Click enable automatic deploy. 
* The live version of the app can be found here.. 

## Technologies Used ## 
* Python 

## Credits ## 
The code for the time was taken from [W3docs](https://www.w3docs.com/snippets/python/how-do-i-measure-elapsed-time-in-python.html/ "W3docs")
The code for display intro function and menu list was taken from [W3resource](https://www.w3resource.com/python-exercises/math/python-math-exercise-63.php/ "W3resource")


## Acknowledgements ## 
Big thank you to my mentor Rory Patrick for all the help throught the project. 

