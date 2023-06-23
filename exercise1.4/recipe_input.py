import pickle

recipes_list = []
all_ingredients = [] 

user_file_request = str(input("Enter a file name --> "))

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
finally: 
    recipes_list = data['recipes_list']
    all_ingredients = data['all_ingredients']


def calc_difficulty(recipe): 
        if recipe['cooking_time'] < 10 and len(recipe['ingredients']) < 4:
            return "easy"
        elif recipe['cooking_time'] < 10 and len(recipe['ingredients']) > 4:
            return "Medium"
        elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) < 4:
            return "Intermediate"
        elif recipe['cooking_time'] >= 10 and len(recipe['ingredients']) >= 4:
            return "Hard"
  

def take_recipe(): 
    name = str(input("Enter the name of the recipe --> "))
    cooking_time = int(input("Enter the cooking time in min (ex: 30) --> "))
    ingredients = []

    ingredient_count = int(input("Enter the number of ingredients for the recipe --> "))
    for _ in range(ingredient_count):
        ingredient = str(input("Enter an ingredient --> ")).lower()
        ingredients.append(ingredient) 
 
    recipe = { 'name' : name, 'cooking_time' : cooking_time, 'ingredients' : ingredients}
    difficulty = calc_difficulty(recipe)
    recipe['difficulty'] = difficulty
     
    return recipe


user_recipe_count = int(input("Enter the number of recipes you would like to add to the recipes list --> "))

for x in range(0, user_recipe_count):
    recipe = take_recipe()
   
    for ingredient in recipe['ingredients']:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)
    
    recipes_list.append(recipe)
    print(" ")
    print(recipe["name"] + " added to recipes list...")
    print(" ")

data['recipes_list'] = recipes_list
data['all_ingredients'] = all_ingredients
 
with open(user_file_request, "wb") as file: 
    pickle.dump(data, file)

print("Data has been written to " + user_file_request)
