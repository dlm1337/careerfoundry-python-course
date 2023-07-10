recipes_list = []
ingredients_list = []
n = int(input("Enter the number of recipes you would like to add to the recipes list --> "))

def take_recipe(): 
    name = str(input("Enter the name of the recipe --> "))
    cooking_time = int(input("Enter the cooking time in min (ex: 30) --> "))
    ingredients = []

    ingredient_count = int(input("Enter the number of ingredients for the recipe --> "))
    for _ in range(ingredient_count):
        ingredient = str(input("Enter an ingredient --> ")).lower()
        ingredients.append(ingredient) 
 
    recipe = { 'name' : name, 'cooking_time' : cooking_time, 'ingredients' : ingredients}
    return recipe

for x in range(0,n):
    recipe = take_recipe()
   
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    
    recipes_list.append(recipe)
    print(" ")
    print(recipes_list[x]["name"] + " added to recipes list...")
    print(" ")

for recipe in recipes_list:
    if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = "Easy"
    elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) > 4:
        recipe['difficulty'] = "Medium"
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
        recipe['difficulty'] = "Intermediate"
    elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
        recipe['difficulty'] = "Hard"

    print("Recipe: " + recipe['name'])
    print("Cooking Time (min): " + str(recipe['cooking_time']))
    print("Ingredients:")
   
    for ingredient in recipe['ingredients']:
        print(ingredient)
 
    print("Difficulty level: " + recipe['difficulty'])
    print(" ")

 
    
ingredients_list.sort()    
print("Ingredients Available Across All Recipes")
print("----------------------------------------")

for ingredient in ingredients_list:
    print(ingredient)

 

