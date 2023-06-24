# Task1.1

The add.py script prompts the user for 2 numbers and adds them together.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage) 
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## Installation

*** This installation assumes you have Python3.8.7 and virtualenvwrapper installed(You have to do this in the command prompt). ***
1. Create a virtual environment.
2. Add requirements.txt to your virtual environment Scripts folder.
3. In vscode activate your environment in the terminal ex: for windows powershell: cd C:\<path to your VirtualEnvs folder>\<environment name>\Scripts\
.\Activate.ps1
4. Write pip install -r requirements.txt
5. Run add.py script inside the directory of your script.


## Usage

When running the script you will be expected to input 2 numbers, then it will print a response adding the 2 numbers together.
 
## Authors

David McNeill

## Acknowledgments

Inspired and instructed by CareerFoundry's Python Course

# Task1.2

 In this task I was expected to use an Ipython shell to store recipe information in a data structure. Then, put each recipe data structure in an outer data structure that stored all recipes.

## Table of Contents

- [Process](#process)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)
 
## Process

 - I added recipes to dictionaries to take advantage of key value pairs. I figured it was a good situation to have the data value labeled with a string key. This makes the code more readable when accessing different parts of the recipe. Dictionaries are also mutable allowing for manipulation to the ingredients if needed. 
  
 - I used a list for the outer structure, being as lists are mutable allowing for modification. If recipes need to be added, manipulated, or removed it can be done easily with a list. Tuples are faster but harder to manipulate as they are immutable. If the outer structure was going to be unchanged, and just added to, a tuple would be the better choice. Each ingredients list was printed on the console by accessing the index of the all_recipes list, and the ingredients key of the dictionary.
 
## Authors

David McNeill

## Acknowledgments

Inspired and instructed by CareerFoundry's Python Course

# Task1.3

The Exercise_1.3.py script prompts the user for how many recipes they would like to add. Then it prompts the user the requirements for the recipe.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage) 
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## Installation

*** This installation assumes you have Python3.8.7 and virtualenvwrapper installed(You have to do this in the command prompt). ***
1. Create a virtual environment. 
2. In vscode activate your environment in the terminal ex: for windows powershell: cd C:\<path to your VirtualEnvs folder>\<environment name>\Scripts\
.\Activate.ps1
3. Run Exercise_1.3.py script inside the directory of your script.


## Usage

When running the script you will be expected to declare how many recipes you would like to add. The recipe's consist of a name, cooking time, and ingredients. When you get to ingredients it will ask how many ingredients you want to add. At the end it will print out the recipes and ingredients across all recipes.
 
## Authors

David McNeill

## Acknowledgments

Inspired and instructed by CareerFoundry's Python Course

# Task1.4

The recipe_input.py script allows the user to add recipes, that are stored in a binary file via the pickle module. In the recipe_search.py the binary file can be accessed to search for recipes that contain a specific ingredient.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage) 
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## Installation

*** This installation assumes you have Python3.8.7 and virtualenvwrapper installed(You have to do this in the command prompt). ***
1. Create a virtual environment for each of your scripts (recipe_input.py, recipe_search.py). 
2. In vscode activate your environments(1 at a time) in the terminal ex: for windows powershell: cd C:\<path to your VirtualEnvs folder>\<environment name>\Scripts\
.\Activate.ps1
3. You can open 2 terminals to have both virtual environments running.
4. Run recipe_input.py script in one terminal.
5. Run recipe_searh.py script in another terminal.
6. You can use recipe_input.bin(pickle binary file) in this github repo as practice data or create your own when running the script.


## Usage

When running the recipe_input.py script you will be expected to input a file name(.bin file). If it is not found it will create the file you typed and start from scratch. You will be prompted how many recipes to add. Then each recipe's name, cooking time, and ingredients. Difficulty will be determined based on the recipe's data. 

When running the recipe_search.py script you will be asked to give the binary file name. All current ingredients in the binary file will be listed to the console. They will be associated with a number. type the number to pull up all recipes that contain the ingredient.
 
## Authors

David McNeill

## Acknowledgments

Inspired and instructed by CareerFoundry's Python Course


