import mysql.connector

conn = mysql.connector.connect(host="localhost", user="cf-python", passwd="password")
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        ingredients VARCHAR(255),
        cooking_time INT,
        difficulty VARCHAR(20)
    )
"""
)
conn.commit()

def main_menu(choice):
    while choice != "quit":
        print("Main Menu")
        print("==============================")
        print("Pick a choice:")
        print("        1. Create a new recipe")
        print("        2. Search for a recipe by ingredient")
        print("        3. Update an existing recipe")
        print("        4. Delete a recipe")
        print("        Type 'quit' to exit the program.")

        choice = str(input("Your choice: "))

        if choice == "1":
            create_recipe()
        elif choice == "2":
            search_recipe()
        elif choice == "3":
            update_recipe()
        elif choice == "4":
            delete_recipe()

def create_recipe():
    try:
        name = str(input("Enter the name of the recipe --> "))
        cooking_time = int(input("Enter the cooking time in min (ex: 30) --> "))
        ingredients = []

        ingredient_count = int(input("Enter the number of ingredients for the recipe --> "))
        for _ in range(ingredient_count):
            ingredient = str(input("Enter an ingredient --> ")).lower()
            ingredients.append(ingredient)
    except:
        print('invalid input for cooking time or ingredient count')
    else:
        ingredients_sql = ", ".join(ingredients)

        difficulty = calculate_difficulty(ingredients, cooking_time)

        sql = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) \
                VALUES (%s, %s, %s, %s)"
        val = (name, ingredients_sql, cooking_time, difficulty)
        cursor.execute(sql, val) 
        conn.commit()

def search_recipe():
    results = cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()

    all_ingredients = []

    for row in results:
        ingredient_list = row[0].split(", ")
        for ingredient in ingredient_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    for i, ingredient in enumerate(all_ingredients, 1):
        print(str(i) + ". " + ingredient)

    try:
        number_picked = int(input("Select an ingredient by entering its number: "))
        if number_picked >= 1 and number_picked <= len(all_ingredients):
            ingredient_searched = all_ingredients[number_picked - 1]
            print("Ingredient searched:", ingredient_searched)
        else:
            print("Invalid number picked.")
    except:
        print("Something went wrong with the last input.")
    else:
        sql = "SELECT * FROM Recipes WHERE ingredients LIKE %s"
        val = ("%" + ingredient_searched + "%",)
        cursor.execute(sql, val)
        results = cursor.fetchall()

        for row in results:
            print("------")
            print("ID: ", row[0])
            print("Name: ", row[1])
            print("Ingredients: ", row[2])
            print("Cooking Time: ", row[3])
            print("Difficulty: ", row[4])
            print("-------")

def update_recipe():
    try:
        all_recipes = fetch_all_recipes()
        column_dict = {1: "name", 2: "ingredients", 3: "cooking_time"}
        update_val = ""

        recipe_id = int(input("pick the number of the recipe to be changed--> "))

        ingredients = all_recipes[recipe_id - 1][2]
        ingredient_list = all_recipes[recipe_id - 1][2].split(", ")
        cooking_time = all_recipes[recipe_id - 1][3]

        print("Columns")
        print("-----------------")
        print("1: Name")
        print("2: Ingredients")
        print("3: Cooking Time")

        column = int(input("Pick the number of the column to update --> "))

        if column == 1:
            update_val = str(input("What would you like to rename the recipe --> "))
        elif column == 2:
            print("Options")
            print("----------------")
            print("1. Add Ingredients")
            print("2. Remove Ingredients")

            option_val = int(input("Pick the number of the option you want -->"))
            if option_val == 1:
                update_val = ingredients_update(ingredient_list)
            else:
                update_val = ingredients_remove(ingredient_list)
        else:
            update_val = int(input("What would you like change the cooking time to --> "))
            update_val = str(update_val)
    except:
        print('you did not use valid numbers for either picking the recipe, cooking time, column, or ingredient option.')
    else:
        if column == 2 or column == 3:
            new_diff = calculate_difficulty(ingredients, int(cooking_time))
            sql = "UPDATE Recipes SET " + column_dict[column] + " = %s WHERE id = %s"
            val = (update_val, recipe_id)
            cursor.execute(sql, val)
            conn.commit()

            sql_difficulty = "UPDATE Recipes SET difficulty = %s WHERE id = %s"
            val_difficulty = (new_diff, recipe_id)
            cursor.execute(sql_difficulty, val_difficulty)
            conn.commit()
        else:
            sql = "UPDATE Recipes SET " + column_dict[column] + " = %s WHERE id = %s"
            val = (update_val, recipe_id)
            cursor.execute(sql, val)
            conn.commit()
            
def delete_recipe():
    try:
        fetch_all_recipes()
        recipe_id = int(input("pick the number of the recipe to be deleted --> "))
    except:
        print('Invalid input for recipe id.')
    else:
        recipe_id = str(recipe_id)
        cursor.execute("DELETE FROM Recipes WHERE id = " + recipe_id) 
        conn.commit()
        cursor.execute("SELECT * FROM Recipes")
        rows = cursor.fetchall()
        cursor.execute("TRUNCATE TABLE Recipes")
        cursor.execute("ALTER TABLE Recipes AUTO_INCREMENT = 1")
        for i, row in enumerate(rows, start=1): 
            reset_id = i
            cursor.execute("INSERT INTO Recipes (id, name, ingredients, cooking_time, difficulty) \
                    VALUES (%s, %s, %s, %s, %s)", (reset_id, row[1], row[2], row[3], row[4])) 
        conn.commit()

def calculate_difficulty(ingredients, cooking_time):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients) > 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        return "Intermediate"
    elif cooking_time >= 10 and len(ingredients) >= 4:
        return "Hard"

def fetch_all_recipes():
    cursor.execute("SELECT * FROM recipes")
    results = cursor.fetchall()
    print("Recipes")
    print("-------------------------")
    for row in results:
        print(str(row[0]) + ": " + row[1])

    return results

def ingredients_update(ingredient_list):
    update_val = []
    print("Ingredients")
    print("------------------")
    for ingredient in ingredient_list:
        print(ingredient)

    ingredient_count = int(
        input("Enter the number of ingredients to add to the recipe --> ")
    )
    for _ in range(ingredient_count):
        ingredient = str(input("Enter name of an ingredient --> ")).lower()
        update_val.append(ingredient)

    ingredient_list.extend(update_val)
    ingredients_sql = ", ".join(ingredient_list)

    return ingredients_sql

def ingredients_remove(ingredient_list):
    update_val = []
    print("Ingredients")
    print("------------------")
    for ingredient in ingredient_list:
        print(ingredient)

    ingredient_count = int(
        input("Enter the number of ingredients to remove from the recipe --> ")
    )
    for _ in range(ingredient_count):
        ingredient = str(input("Enter name of an ingredient --> ")).lower()
        update_val.append(ingredient)

    for ingredient in update_val:
        if ingredient in ingredient_list:
            ingredient_list.remove(ingredient)

    ingredients_sql = ", ".join(ingredient_list)

    return ingredients_sql

choice = ''
main_menu(choice)
conn.close()
