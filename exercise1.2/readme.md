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