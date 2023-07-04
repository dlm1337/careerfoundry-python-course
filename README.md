# CareerFoundry Python Course

This repository contains exercises and scripts for the CareerFoundry Python course.

## Table of Contents  
- [Exercise_1.1](#exercise_11)
  - [Installation](#exercise_11-installation)
  - [Usage](#exercise_11-usage)
- [Exercise_1.2](#exercise_12)
  - [Process](#exercise_12-process)
- [Exercise_1.3](#exercise_13)
  - [Installation](#exercise_13-installation)
  - [Usage](#exercise_13-usage)
- [Exercise_1.4](#exercise_14)
  - [Installation](#exercise_14-installation)
  - [Usage](#exercise_14-usage)
- [Exercise_1.5](#exercise_15)
  - [Installation](#exercise_15-installation)
  - [Usage](#exercise_15-usage)
- [Exercise_1.6](#exercise_16)
  - [Installation](#exercise_16-installation)
  - [Usage](#exercise_16-usage)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)
 
 ------------------------------------------------------------------------------------------------------------------------
 ------------------------------------------------------------------------------------------------------------------------

## Exercise_1.1

The `add.py` script prompts the user for two numbers and adds them together.

------------------------------------------------------------------------------------------------------------------------

### Exercise_1.1-Installation

To install and run the script, follow these steps:

1. Ensure you have Python 3.8.7 and `virtualenvwrapper` installed.
2. Create a virtual environment for the project.
3. Add `requirements.txt` to your virtual environment's Scripts folder.
4. Activate the virtual environment in your terminal or command prompt.
5. Install the dependencies by running `pip install -r requirements.txt`.
6. Run the `add.py` script inside the directory of your script.

------------------------------------------------------------------------------------------------------------------------

### Exercise_1.1-Usage

When running the `add.py` script, you will be prompted to enter two numbers. The script will then add them together and display the result.

------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------

## Exercise_1.2

This task involves using an IPython shell to store recipe information in data structures.

------------------------------------------------------------------------------------------------------------------------

### Exercise_1.2-Process

- Recipes are stored as dictionaries to take advantage of key-value pairs.
- An outer data structure, which is a list, is used to store all recipes.
- Each recipe dictionary contains the necessary information such as name, cooking time, and ingredients.
- The list of all recipes can be accessed to display the recipe information.

------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------

## Exercise_1.3

The `Exercise_1.3.py` script prompts the user to input recipe information.

------------------------------------------------------------------------------------------------------------------------

### Exercise_1.3-Installation

To install and run the script, follow these steps:

1. Ensure you have Python 3.8.7 and `virtualenvwrapper` installed.
2. Create a virtual environment for the project.
3. Activate the virtual environment in your terminal or command prompt.
4. Run the `Exercise_1.3.py` script inside the directory of your script.

### Exercise_1.3-Usage

------------------------------------------------------------------------------------------------------------------------

When running the `Exercise_1.3.py` script, you will be prompted to enter the number of recipes you want to add. For each recipe, you will enter its name, cooking time, and ingredients. The script will then display the recipes and their ingredients.

------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------

## Exercise_1.4

The `recipe_input.py` script allows the user to add recipes, which are stored in a binary file using the `pickle` module. The `recipe_search.py` script can be used to search for recipes based on a specific ingredient.

------------------------------------------------------------------------------------------------------------------------

### Exercise_1.4-Installation

To install and run the scripts, follow these steps:

1. Ensure you have Python 3.8.7
2. Create a virtual environment for each script (`recipe_input.py` and `recipe_search.py`).
3. Activate the virtual environments in separate terminals.
4. Run the `recipe_input.py` script in one terminal.
5. Run the `recipe_search.py` script in another terminal.
6. You can use `recipe_input.bin` (pickle binary file) in this GitHub repo as practice data or create your own when running the script.

------------------------------------------------------------------------------------------------------------------------

### Exercise_1.4-Usage

- When running the `recipe_input.py` script, you will be prompted to input a file name (`.bin` file). If the file is not found, it will create a new file with the given name and start from scratch. You will then be asked how many recipes to add, followed by the details of each recipe (name, cooking time, ingredients). The difficulty of each recipe will be determined based on its data.
- When running the `recipe_search.py` script, you will be asked to provide the binary file name. The script will list all current ingredients in the binary file along with their associated numbers. You can enter a number to display all recipes that contain the corresponding ingredient.

------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------

## Exercise_1.5

The `recipe_oop.py` script has created a class to create and manipulate Recipe objects. 

------------------------------------------------------------------------------------------------------------------------

### Exercise_1.5-Installation

To install and run the scripts, follow these steps:

1. Ensure you have Python 3.8.7
2. Create a virtual environment for the script (`recipe_oop.py`).
3. Activate the virtual environments in the terminal.
4. Run the `recipe_oop.py` script. 
6. Some basic operations are already creating Recipe objects to test the class functionality.

------------------------------------------------------------------------------------------------------------------------

### Exercise_1.5-Usage

- When running the `recipe_oop.py` you can perform basic operations to the objects created by the Recipe class. You can set all the properties at the object creation(name, cooking time, ingredients),
and difficulty will be set automatically. You can come back and change these properties later if you
would like with the custom getter and setter methods. It will also recalculate difficulty if cooking time, or ingredients are changed. You can add more ingredients to the objects later on, and there is a class variable that will store unique ingredients accross all objects. You can also preform a search based on a specific ingredient with the recipe_search method inside the class. The recipe_search method
will search through a provided list of Recipe objects, and you must provide a keyword as well to search for. If cooking time and/or ingredients are left out the object should still be created, and have the ability to add these properties later. This is thanks to the try/catch blocks.

------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------

## Exercise_1.6

The `recipe_mysql.py` script allows the user to create and manipulate recipes in a continuous flow, until the user is ready to quit.

------------------------------------------------------------------------------------------------------------------------

### Exercise_1.6-Installation

To install and run the scripts, follow these steps:

1. Ensure you have Python 3.8.7
2. Create a virtual environment for the script (`recipe_mysql.py`).
3. Activate the virtual environments in the terminal.
4. Run the `recipe_mysql.py` script. 
6. Perform operations in the terminal choosing from 5 choices.
7. type quit in the main menu to stop the script from running.

------------------------------------------------------------------------------------------------------------------------

### Exercise_1.6-Usage

- When running the `recipe_mysql.py` you are brought to the main menu in the terminal. You can choose from 5 options to perform C.R.U.D operations on your Recipe database. The Recipe database will be created if not already on the system. The program will loop until you are done manipulating recipe data by typing quit in the main menu.  

------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------

## Authors

David McNeill

------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------

## Acknowledgments

Inspired and instructed by CareerFoundry's Python Course