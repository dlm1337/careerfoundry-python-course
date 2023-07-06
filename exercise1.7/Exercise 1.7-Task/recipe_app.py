from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
## Recipe class is imported for less clutter.
import recipe_class

## sqlalchemy create_engine establishes connection with the mysql database.
engine = create_engine("mysql://cf-python:password@localhost/task_database")

## sqlalchemy sessionmaker allows for running queries on the selected db.
Session = sessionmaker(bind=engine)
session = Session()

recipe_class.Recipe.metadata.create_all(engine)

## create_recipe prompts the user for the recipe name, ingredients, and cooking time.
#  It creates a new recipe object that calculates the difficulty automatically. If an
#  invalid input is entered it should prompt the user accordingly and return to the
#  main menu.
def create_recipe():
    try:
        name = input("Enter the name of the recipe --> ").lower().capitalize()
        ingredients = []

        ingredient_count = input("Enter the number of ingredients for the recipe(max: 20) --> ")
        if not ingredient_count.isdigit() or int(ingredient_count) > 20 or int(ingredient_count) < 1:
            print('invalid numbers were entered. Back to the main menu...')
            return

        for _ in range(int(ingredient_count)):
            ingredient = input("Enter an ingredient --> ").lower().capitalize()
            ingredients.append(ingredient)
        ## unique_ingredients makes sure the user is not putting in the same thing more than once.
        unique_ingredients = list(set(ingredients))

        cooking_time = input("Enter the cooking time in min (ex: 30) --> ")
        if not cooking_time.isdigit():
            print('invalid cooking time. Back to the main menu...')
            return
        ## Adds the new recipe made by the user to the recipe table.
        ingredients_str = ", ".join(unique_ingredients)
        recipe_entry = recipe_class.Recipe(name, ingredients_str, int(cooking_time))
        session.add(recipe_entry)
        session.commit()
    except Exception as e:
        print('Unexpected Error: ', str(e))

## view_all_recipes() will display all available recipes in a well formatted manor with __str__().
 # If there are no recipes available it will prompt the user and return to main menu.
def view_all_recipes():
    try:
        recipes = session.query(recipe_class.Recipe).all()
        if not recipes:
            print("There are no recipes currently available. Try creating some from the main menu.")
            return None

        for recipe in recipes: 
            print(recipe.__str__())
    except Exception as e:
        print('Unexpected Error: ', str(e))

## search_by_ingredients will check if recipes are available first. If not it will return to the
#  main menu after prompting the user. It will then grab all unique ingredients, and ask the user
#  which ingredients to search by. If there are any invalid inputs the user will be prompted
#  accordingly and returned to the main menu.
def search_by_ingredients(): 
    try:
        if session.query(recipe_class.Recipe).count() == 0:
            print("There are no recipes currently available. Try creating some from the main menu.")
            return
        ## results is a gathering of all ingredients across all recipes. It then is checked for duplicates
        #  in the double for loop. It is split into a list from its string form as well.
        results = session.query(recipe_class.Recipe.ingredients).all()
    
        all_ingredients = []
    
        for ingredients_str in results:
            temp_list = ingredients_str[0].split(", ")
            for ingredient in temp_list:
                if ingredient not in all_ingredients:
                    all_ingredients.append(ingredient)
        ## print all the ingredients that can be searched by.
        print("\n" + "Searchable Ingredients:")
        print("-"*20)
    
        for i, ingredient in enumerate(all_ingredients, 1):
            print(str(i) + ": " + ingredient)
        print("\n")

        numbers_picked_str = input("Search ingredients by its number separated by spaces-->  ").split()
    
        search_ingredients = []
        ## checks all numbers picked by the user for associated ingredient.
        for num in numbers_picked_str:
            if not num.isdigit() or int(num) < 1 or int(num) > len(all_ingredients):
                print('Invalid input. Please enter valid numbers.')
                return
            i = int(num) - 1
            ingredient = all_ingredients[i]
            search_ingredients.append(ingredient)
        ## terms to search for in the recipes are put into a list.
        conditions = []
    
        for ingredient in search_ingredients:
            like_term = "%" + ingredient + "%"
            conditions.append(recipe_class.Recipe.ingredients.like(like_term)) 

        recipes = session.query(recipe_class.Recipe).filter(*conditions).all()

        for recipe in recipes:
            print(recipe.__str__())
    except Exception as e:
        print('Unexpected Error: ', str(e))
        
## edit_recipe() first checks if there any recipes and prompts the user if there is not. Then grabs
#  all the recipes and list the based on there id. All user prompts are validated for correct input.
#  If a correct input is picked the user picks an attribute to be changed. After changing an input
#  the recipe is updated in the database at the given id. All inputs should be validated or the user
#  will be returned to the main menu.
def edit_recipe(): 
    try:
        if session.query(recipe_class.Recipe).count() == 0:
            print("There are no recipes currently available. Try creating some from the main menu.")
            return
    
        ## This queres the id and name to print a formatted list for the user to choose a number for a recipe to edit.
        results = session.query(recipe_class.Recipe.id, recipe_class.Recipe.name).all()
        
        print(" ")
        print("All Recipes:")
        print("-"*20)

        for id, name in results:
            print(str(id) + ': ' + name)
        print(" ")
    
        id_picked = input("Pick a recipe to edit based on its associated number--> ")
        
        if not id_picked.isdigit():
            print('You are using non numeric characters, or decimals to pick a recipe number. ' \
                   + 'Back to the main menu...')
            return
        ## check that this id is a number within the range or recipes.
        recipe_id_valid = False
        
        for x in range(len(results)):
            if results[x][0] == int(id_picked):
                recipe_id_valid = True
                break
    
        if not recipe_id_valid:
            print("The number given is not in range of the available recipe numbers. " \
                   + "Back to the main menu...")
            return
        ## recipe_to_edit queries the first row to come back with the id provided by the user.
        recipe_to_edit = session.query(recipe_class.Recipe).filter(recipe_class.Recipe.id == id_picked).first()
    
        print(" ")
        print("Recipe to Edit:")
        print("-"*20) 
        print("1. Name: " + recipe_to_edit.name)
        print("2. Ingredients: " + recipe_to_edit.ingredients)
        print("3. Cooking Time: " + str(recipe_to_edit.cooking_time) + "\n") 
    
        recipe_attr_num = input("Pick a number to change part of the recipe(difficulty is auto-calculated)--> ")
        ## make sure user picks valid attribute.
        if not recipe_attr_num.isdigit():
            print('You are using non numeric characters, or decimals to pick a recipe attribute. ' \
                   + 'Back to the main menu...')
            return
        
        if recipe_attr_num == "1":
            new_name = input("What do you want to re-name " + recipe_to_edit.name + "--> ").lower().capitalize()
            recipe_to_edit.name = new_name
            
        elif recipe_attr_num == "2":
            print(" ")
            print("Options: ")
            print("-"*20)
            print("1. Add Ingredients")
            print("2. Remove Ingredients" + "\n")

            add_or_remove_num = input("Pick an option to edit ingredients for " \
                                        + recipe_to_edit.name + "--> ")
            ## make sure user user picks 1 or 2.
            if not add_or_remove_num.isdigit():
                print('You are using non numeric characters, or decimals to pick a recipe number. ' \
                      +'Back to the main menu...')
                return 
            
            if add_or_remove_num != '1' and add_or_remove_num != '2':
                print('You did not select either 1 or 2. Back to the main menu...')
                return

            if add_or_remove_num == '1':
                ## calls a Recipe class method to handle logic of adding as many ingredients as user wishes.
                new_ingredients = recipe_to_edit.ingredients_add() 
                if new_ingredients =='invalid':
                    print('Invalid input for amount of ingredients to add. Back to main menu...')
                    return
                recipe_to_edit.ingredients = new_ingredients 
            elif add_or_remove_num == '2':
                ## calls a Recipe class method to handle logic of removing as many ingredients as user wishes.
                new_ingredients = recipe_to_edit.ingredients_remove() 
                if new_ingredients =='invalid':
                    print('Invalid input for amount of ingredients to remove. Back to main menu...')
                    return
                recipe_to_edit.ingredients = new_ingredients 

        elif recipe_attr_num == "3":
            new_cooking_time = input("Enter the new cooking time for " + recipe_to_edit.name + "--> ")
            ## make sure user picks valid cooking time.
            if not str(new_cooking_time).isdigit():
                print('invalid cooking time. Back to the main menu...')
                return
            recipe_to_edit.cooking_time = int(new_cooking_time) 
        else:
            print("Invalid attribute picked. Back to the main menu...")
            return
        ##  The following query updates the recipe picked by the user by finding its id and replacing
        #   any newly changed attributes frome the recipe_to_edit.
        update_recipe = recipe_class.Recipe(recipe_to_edit.name, recipe_to_edit.ingredients, recipe_to_edit.cooking_time)
       
        session.query(recipe_class.Recipe).filter(recipe_class.Recipe.id == update_recipe.id) \
               .update({recipe_class.Recipe.name: update_recipe.name, recipe_class.Recipe.ingredients: \
                update_recipe.ingredients, recipe_class.Recipe.cooking_time: update_recipe.cooking_time})
        
        session.commit()
        print('Recipe changed.' + '\n') 
    except Exception as e:
        print('Unexpected Error: ', str(e))

## delete_Recipe will check that recipes exist first. Then it will list out available recipes. The user
#  picks a number that is run through some validation code. If it passes the user is asked if they are 
#  sure they want to delete the recipe. If they are the ids of the recipes are recalculated to keep it neat.
def delete_recipe():
    try:
        if session.query(recipe_class.Recipe).count() == 0:
            print("There are no recipes currently available. Try creating some from the main menu.")
            return
        
        ## This queres the id and name to print a formatted list for the user to choose a number for a recipe to delete.
        results = session.query(recipe_class.Recipe.id, recipe_class.Recipe.name).all()
        
        print(" ")
        print("All Recipes:")
        print("-"*20)

        for id, name in results:
            print(str(id) + ': ' + name)
        print(" ")
    
        id_picked = input("Pick a recipe to delete based on its associated number--> ")
        
        if not id_picked.isdigit():
            print('You are using non numeric characters, or decimals to pick a recipe number. ' \
                  + 'Back to the main menu...')
            return
        ## check that this id is a number within the range or recipes.
        recipe_id_valid = False
        
        for x in range(len(results)):
            if results[x][0] == int(id_picked):
                recipe_id_valid = True
                break
    
        if not recipe_id_valid:
            print("The number given is not in range of the available recipe numbers. " \
                   + "Back to the main menu...")
            return

        ## This queries only the recipe associated with the picked id.  
        recipe = session.query(recipe_class.Recipe).filter(recipe_class.Recipe.id == id_picked).first()
    
        delete_recipe = input("<CAUTION!>Type all lower case 'yes' to delete " + recipe.name + \
                            " or 'anything' to cancel--> ")

        if delete_recipe.lower() == "yes": 
            session.delete(recipe)
        else:
            print("You canceled the delete.")
            return
        
        ## Below is an effort to keep the id's neat as things are deleted. It grabs all rows in the
        #  Recipe table and stores to a variable called rows. Then deletes the recipe table. Then
        #  adds the rows back with new ids so it will stay in order.
        # Retrieve all rows from the Recipes table
        rows = session.query(recipe_class.Recipe).all() 
        session.query(recipe_class.Recipe).delete()
        
        for i, row in enumerate(rows, start=1):
            recipe_with_new_id = recipe_class.Recipe(row.name, row.ingredients, row.cooking_time)
            recipe_with_new_id.id = i; 
            session.add(recipe_with_new_id)
 
        session.commit()
        print("Recipe: " + recipe.name + " deleted...")               
    except Exception as e:
        print('Unexpected Error: ', str(e))

## The main menu will loop till the user types quit. All above functions are available in the main menu.
choice = ''
def main_menu(choice):
    while choice != "quit":
        print("")
        print("Main Menu")
        print("==============================")
        print("Pick a choice:")
        print("        1. Create a new recipe")
        print("        2. View all recipes")
        print("        3. Search for recipes by ingredients.")
        print("        4. Edit a recipe.")
        print("        5. Delete a recipe.")
        print("        Type 'quit' to quit the application.")
        print(" ")

        choice = str(input("Your choice: "))
        print(" ")

        if choice == "1":
            create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            search_by_ingredients()
        elif choice == "4":
            edit_recipe()
        elif choice == "5":
            delete_recipe()
        else:
            if choice != 'quit':
                print('The input was invalid.')

main_menu(choice)




