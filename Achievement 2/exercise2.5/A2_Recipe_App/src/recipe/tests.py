from django.test import TestCase, Client
from .models import Recipe
from django.core.exceptions import ValidationError
from recipeingredient.models import RecipeIngredient
from ingredient.models import Ingredient
from recipeingredientintermediary.models import RecipeIngredientIntermediary

# Create your tests here.


class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(
            title="Nachos",
            directions="Put nachos on a plate with cheese, cook in microwave. Add sour cream, jalapenos, salsa, and lettuce.",
            cooking_time=3,
            star_count=5,
            recipe_type="snack",
            adapted_link="https://nachos.com",
            servings=3,
            yield_amount=12,
            allergens="unknown",
        )
        Recipe.objects.create(
            title="Pancakes",
            directions="Mix ingredients, cook on a griddle, serve with syrup.",
            cooking_time=9,
            star_count=4,
            recipe_type="breakfast",
            servings=2,
        )
        Recipe.objects.create(
            title="Pizza",
            directions="Make dough, add toppings, bake in the oven.",
            cooking_time=30,
            star_count=3,
            recipe_type="dinner",
            servings=4,
        )
        Recipe.objects.create(
            title="Smoothie",
            directions="Blend fruits and yogurt together.",
            cooking_time=10,
            star_count=5,
            recipe_type="snack",
            servings=1,
        )
        Recipe.objects.create(
            title="Test Recipe 1",
            directions="Test Directions",
            cooking_time=10,
            star_count=5,
            recipe_type="breakfast",
            servings=4,
        )
        Recipe.objects.create(
            title="Test Recipe 2",
            directions="Test Directions",
            cooking_time=30,
            star_count=3,
            recipe_type="dinner",
            servings=2,
        )
        Recipe.objects.create(
            title="Test Recipe 3",
            directions="Test Directions",
            cooking_time=20,
            star_count=3,
            recipe_type="lunch",
            servings=3,
        )
        Recipe.objects.create(
            title="Test Recipe 4",
            directions="Test Directions",
            cooking_time=15,
            star_count=4,
            recipe_type="snack",
            servings=1,
            yield_amount=0,
        )
        ri1 = RecipeIngredient.objects.create(
            ingredient=Ingredient.objects.create(name="Ingredient 1"),
            calorie_content=20,
            amount=1.5,
            amount_type="cup",
            cost=20.40,
            supplier="supplier",
            grams=20.22,
        )

        ri2 = RecipeIngredient.objects.create(
            ingredient=Ingredient.objects.create(name="Ingredient 2"),
            calorie_content=10,
            amount=0.5,
            amount_type="teaspoon",
            cost=5.10,
            supplier="supplier",
            grams=5.25,
        )

        ri3 = RecipeIngredient.objects.create(
            ingredient=Ingredient.objects.create(name="Ingredient 3"),
            calorie_content=30,
            amount=2,
            amount_type="tablespoon",
            cost=10.15,
            supplier="supplier",
            grams=25.50,
        )

        ri4 = RecipeIngredient.objects.create(
            ingredient=Ingredient.objects.create(name="Ingredient 4"),
            calorie_content=30,
            amount=2,
            amount_type="tablespoon",
            cost=10.15,
            supplier="supplier",
            grams=25.50,
        )

        # Retrieve the Recipe instance and associate RecipeIngredients with it
        recipe = Recipe.objects.get(id=1)
        recipe.recipe_ingredients.add(ri1)

        recipe2 = Recipe.objects.get(id=2)
        recipe2.recipe_ingredients.add(ri1, ri2, ri3, ri4)

    def test_recipe_title(self):
        recipe = Recipe.objects.get(id=1)

        field_label = recipe._meta.get_field("title").verbose_name

        self.assertEqual(field_label, "title")

    def test_recipe_directions(self):
        recipe = Recipe.objects.get(id=1)
        expected_directions = "Put nachos on a plate with cheese, cook in microwave. Add sour cream, jalapenos, salsa, and lettuce."
        self.assertEqual(recipe.directions, expected_directions)

    def test_recipe_cooking_time(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.cooking_time, 3)

    def test_recipe_star_count(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.star_count, 5)

    def test_recipe_recipe_type(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.recipe_type, "snack")

    def test_recipe_adapted_link(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.adapted_link, "https://nachos.com")

    def test_recipe_servings(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.servings, 3)

    def test_recipe_yield_amount(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.yield_amount, 12)

    def test_recipe_allergens(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.allergens, "unknown")

    def test_recipe_id_auto_increment(self):
        recipe1 = Recipe.objects.get(id=2)
        recipe2 = Recipe.objects.get(id=3)
        self.assertEqual(recipe1.id, 2)
        self.assertEqual(recipe2.id, 3)

    def test_recipe_yield_amount_blank(self):
        recipe = Recipe.objects.get(id=4)
        self.assertIsNone(recipe.yield_amount)

    def test_recipe_cooking_time_not_negative(self):
        recipe = Recipe(cooking_time=-10)
        with self.assertRaises(ValidationError):
            recipe.clean_fields(exclude=["id"])

    def test_recipe_star_count_not_negative(self):
        recipe = Recipe(star_count=-2)
        with self.assertRaises(ValidationError):
            recipe.clean_fields(exclude=["id"])

    def test_recipe_servings_not_negative(self):
        recipe = Recipe(servings=-3)
        with self.assertRaises(ValidationError):
            recipe.clean_fields(exclude=["id"])

    def test_recipe_yield_amount_not_negative(self):
        recipe = Recipe(yield_amount=-1)
        with self.assertRaises(ValidationError):
            recipe.clean_fields(exclude=["id"])

    def test_get_absolute_url(self):
        # testing details page link.
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), "/list/1")

    def test_home_page_link(self):
        # testing home page.
        client = Client()
        response = client.get("/")

        self.assertEqual(response.status_code, 200)

    def test_calculate_difficulty_easy(self):
        # Create RecipeIngredientIntermediary instances to associate RecipeIngredients with the Recipe
        RecipeIngredientIntermediary.objects.create(
            recipe=Recipe.objects.get(id=1),
            recipe_ingredient=RecipeIngredient.objects.get(id=1),
        )

        recipe = Recipe.objects.get(id=1)

        result = recipe.calculate_difficulty()

        self.assertEqual(result, "Easy")

    def test_calculate_difficulty_medium(self):
        recipe = Recipe.objects.get(id=2)
        RecipeIngredientIntermediary.objects.create(
            recipe=Recipe.objects.get(id=2),
            recipe_ingredient=RecipeIngredient.objects.get(id=1),
        )
        RecipeIngredientIntermediary.objects.create(
            recipe=Recipe.objects.get(id=2),
            recipe_ingredient=RecipeIngredient.objects.get(id=2),
        )
        RecipeIngredientIntermediary.objects.create(
            recipe=Recipe.objects.get(id=2),
            recipe_ingredient=RecipeIngredient.objects.get(id=3),
        )
        RecipeIngredientIntermediary.objects.create(
            recipe=Recipe.objects.get(id=2),
            recipe_ingredient=RecipeIngredient.objects.get(id=4),
        )
        result = recipe.calculate_difficulty()

        self.assertEqual(result, "Medium")

    def test_calculate_difficulty_missing_data(self):
        # Test for missing cooking time or ingredients
        # The method should return "Missing cooking time or ingredients." when forced into
        # exception
        recipe = Recipe()
        result = recipe.calculate_difficulty()
        self.assertEqual(result, "Missing cooking time or ingredients.")
