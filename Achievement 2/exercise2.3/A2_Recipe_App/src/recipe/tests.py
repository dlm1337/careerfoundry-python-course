from django.test import TestCase
from .models import Recipe
from django.core.exceptions import ValidationError

# Create your tests here.


class RecipeModelTest(TestCase):
    def setUpTestData():
        Recipe.objects.create(
            title="Nachos",
            directions="Put nachos on a plate with cheese, cook in microwave. Add sour cream, jalapenos, salsa, and lettuce.",
            cooking_time=50,
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
            cooking_time=20,
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
        self.assertEqual(recipe.cooking_time, 50)

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
