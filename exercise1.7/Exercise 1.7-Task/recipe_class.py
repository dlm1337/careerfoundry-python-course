from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, String
from sqlalchemy import Column

## Base is inherited by the Recipe class and allows sqlalchemy to interpet the table to find or create.
Base = declarative_base()

class Recipe(Base):
   
    ## table to create with rows defined below.
    __tablename__ = "final_recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))
    
    ## class constructor. Automatically called when the class makes an object.
    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.calculate_difficulty()
   
    ## __repr__() prints a shortly formatted version of the recipe.
    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + '-' + self.difficulty + ">"
   
    ## __str__() prints a well formatted full version of the recipe.
    def __str__(self):
        temp_ingredients = self.ingredients.split(", ")
        recipe_input =  '-'*20 + '\n' \
                        + 'Recipe: ' + self.name + '\n' \
                        + 'Cooking Time (min): ' + str(self.cooking_time) + '\n' \
                        + 'Difficulty level: ' + self.difficulty + '\n'
        
        recipe_ingredients_input = 'Ingredients: ' + '\n'

        for ingredient in temp_ingredients:
            recipe_ingredients_input += ingredient
            recipe_ingredients_input += '\n'

        return recipe_input + recipe_ingredients_input
    
    ## calculate_difficulty is auto in create_recipe(), however need to be called 
    #  if editing a recipe(called in edit_recipe()).
    def calculate_difficulty(self):
        try:
            ingredients_list = self.return_ingredients_as_list()
            if self.cooking_time < 10 and len(ingredients_list) < 4:
                self.difficulty = "Easy"
            elif self.cooking_time < 10 and len(ingredients_list) > 4:
                self.difficulty = "Medium"
            elif self.cooking_time >= 10 and len(ingredients_list) < 4:
                self.difficulty = "Intermediate"
            elif self.cooking_time >= 10 and len(ingredients_list) >= 4:
                self.difficulty = "Hard"
        except: 
            print('Missing an appropriate cooking time or ingredients.')
            self.difficulty = ''
    
    ## returns the ingredients as a list, checks if there are ingredients.
    def return_ingredients_as_list(self):
        if not self.ingredients: 
            return []
 
        ingredients_list = self.ingredients.split(", ")
        return ingredients_list
    
    ## ingredients_add was added to the class to make ingredient changing 
    #  easier(called by edit_recipe()).
    def ingredients_add(self):
        ingredients_list = self.return_ingredients_as_list()
        update_val = [] 

        ingredient_count = input("Enter the number of ingredients to add to the recipe(max: 5) --> ")
     
        if not ingredient_count.isdigit() or int(ingredient_count) > 5 or int(ingredient_count) < 1:
            return 'invalid'

            
        for _ in range(int(ingredient_count)):
            ingredient = input("Enter name of an ingredient --> ").lower().capitalize()
            update_val.append(ingredient)

        ingredients_list.extend(update_val)
        ## using set to get unique values then converting back to a list.
        unique_list = list(set(ingredients_list))
        ingredients_sql_str = ", ".join(unique_list)

        return ingredients_sql_str
    
    ## ingredients_remove was added to the class to make ingredient 
    #  removing easier(called by edit_recipe()).
    def ingredients_remove(self):
        ingredients_list = self.return_ingredients_as_list()
        update_val = [] 

        ingredient_count = input("Enter the number of ingredients to remove from the recipe(max: 5) --> ")
        
        if not ingredient_count.isdigit() or int(ingredient_count) > 5 or int(ingredient_count) < 1:
            return 'invalid'

        for _ in range(int(ingredient_count)):
            ingredient = input("Enter name of an ingredient --> ").lower().capitalize()
            update_val.append(ingredient)

        for ingredient in update_val:
            if ingredient in ingredients_list:
                ingredients_list.remove(ingredient)

        ingredients_sql_str = ", ".join(ingredients_list)

        return ingredients_sql_str
