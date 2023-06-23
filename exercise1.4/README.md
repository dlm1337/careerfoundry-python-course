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
