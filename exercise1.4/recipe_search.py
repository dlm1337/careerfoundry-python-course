import pickle

def display_recipe(recipe):
    print("Recipe: " + recipe['name'])
    print(" ")
    print("Cooking Time (min): " + str(recipe['cooking_time']))
    print(" ")
    print("Ingredients:")
   
    for ingredient in recipe['ingredients']:
        print(ingredient)
    print(" ")
    print("Difficulty level: " + recipe['difficulty'])
    print(" ")

def search_ingredient(data):
    all_ingredients = data['all_ingredients']
    print("All Ingredients:")
    for i, ingredient in enumerate(all_ingredients, 1):
        print(str(i) + ". " + ingredient)

    try:
        number_picked = int(input("Select an ingredient by entering its number: "))
        if  number_picked >= 1 and number_picked <= len(all_ingredients):
            ingredient_searched = all_ingredients[number_picked - 1]
            print("Ingredient searched:", ingredient_searched)
        else:
            print("Invalid number picked.")
    except:
        print('Something went wrong with the last input.')
    else:
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
                display_recipe(recipe)


user_file_request = str(input("What is the name of the file that contains your recipe data? "))

try:
    user_file = open(user_file_request, 'rb')
    data = pickle.load(user_file)
except FileNotFoundError:
    print("File with the given name is not found.") 
    data = {'recipes_list': [] , 'all_ingredients': []} 
except:
    print("Unexpected Error.")  
    data = {'recipes_list': [] , 'all_ingredients': []} 
else:
    user_file.close()
    search_ingredient(data)

# data = {'recipes_list': [{'name': 'lemonade', 'cooking_time':5, 
#         'difficulty': 'EASY', 'ingredients':['sugar', 'water', 'lemons']}],
#         'all_ingredients': ['sugar', 'water', 'lemons']}
# search_ingredient(data)



    