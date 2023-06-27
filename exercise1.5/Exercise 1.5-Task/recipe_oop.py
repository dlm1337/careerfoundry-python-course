class Recipe(object):
 
    all_ingredients = []

    def __init__(self, name, ingredients, cooking_time):
        self.name = name
        self.ingredients = ingredients
        self.cooking_time = cooking_time
        self.difficulty = Recipe.calculate_difficulty(self)
        Recipe.update_all_ingredients(self)

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_cooking_time(self):
        return self.cooking_time
    
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
        self.difficulty = Recipe.calculate_difficulty(self)

    def add_ingredients(self, *ingredients):
        for ingredient in ingredients:
            if ingredient not in self.ingredients:
                self.ingredients.append(ingredient)
        Recipe.update_all_ingredients(self)
        self.difficulty = Recipe.calculate_difficulty(self)

    def get_ingredients(self):
        return self.ingredients
    
    def calculate_difficulty(self):
        try:
            if self.cooking_time < 10 and len(self.ingredients) < 4:
                return "Easy"
            elif self.cooking_time < 10 and len(self.ingredients) > 4:
                return "Medium"
            elif self.cooking_time >= 10 and len(self.ingredients) < 4:
                return "Intermediate"
            elif self.cooking_time >= 10 and len(self.ingredients) >= 4:
                return "Hard"
        except: 
            self.difficulty = ''

    def get_difficulty(self):
            if len(self.difficulty) > 0:
                return self.difficulty
            else:
                return Recipe.calculate_difficulty(self) 

    def search_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            return True
        else:
            return False
        
    def update_all_ingredients(self):
        try:
            for ingredient in self.ingredients:
                if ingredient not in Recipe.all_ingredients:
                    Recipe.all_ingredients.append(ingredient)
        except:
            self.ingredients = []

    def __str__(self):
        recipe_input =  '---------------------------------------------------------' + '\n' \
                        + 'Recipe: ' + self.name + '\n' + '\n' \
                        + 'Cooking Time (min): ' + str(self.cooking_time) + '\n' + '\n' \
                        + 'Difficulty level: ' + self.difficulty + '\n' + '\n'
        
        recipe_ingredients_input = 'Ingredients: ' + '\n'

        for ingredient in self.ingredients:
            recipe_ingredients_input += ingredient
            recipe_ingredients_input += '\n'

        return recipe_input + recipe_ingredients_input
    
    def recipe_search(self, *data, search_term):
        for recipe in data:
            satisfied = recipe.search_ingredient(search_term)
            if satisfied:
                print(recipe)
             

tea = Recipe('Tea', None, None)
tea.add_ingredients(*['Tea Leaves', 'Sugar', 'Water']) 
tea.set_cooking_time(5)

coffee = Recipe('Coffee',['Coffee Powder', 'Sugar', 'Water'], 5)
cake = Recipe('Cake', ['Sugar', 'Butter', 'Eggs', 'Vanilla Essence', 'Flour', 'Baking Powder', 'Milk'], 50)
banana_smoothie = Recipe('Banana Smoothie', ['Bananas', 'Milk', 'Peanut Butter', 'Sugar', 'Ice Cubes'], 5)

recipes_list = [tea, coffee, cake, banana_smoothie]
tea.recipe_search(*recipes_list, search_term = 'Bananas')


     


  


