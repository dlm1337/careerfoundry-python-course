import os
import uuid
from django.test import TestCase, Client, override_settings
from .models import Recipe
from django.core.exceptions import ValidationError
from recipeingredient.models import RecipeIngredient
from ingredient.models import Ingredient
from recipeingredientintermediary.models import RecipeIngredientIntermediary
from django.core.files import File
from customuser.models import CustomUser
from .forms import RecipeSearchForm

# Create your tests here.


class RecipeModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a fake user
        cls.user = CustomUser.objects.create(
            username="fakeuser",
            email="fake@example.com",
            password="testpassword",
        )

        # Create Recipe objects and associate them with the fake user
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
            user=cls.user,
        )
        Recipe.objects.create(
            title="Pancakes",
            directions="Mix ingredients, cook on a griddle, serve with syrup.",
            cooking_time=9,
            star_count=4,
            recipe_type="breakfast",
            servings=2,
            user=cls.user,
        )
        recipe = Recipe.objects.create(
            title="Test Recipe",
            directions="Test Directions",
            cooking_time=15,
            star_count=4,
            recipe_type="snack",
            servings=1,
            user=cls.user,
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

    @override_settings(
        MEDIA_ROOT="/tmp"
    )  # Override the MEDIA_ROOT setting to use a temporary directory
    def test_recipe_pic(self):
        # Use the existing "no_picture.jpg" from the media folder
        image_path = os.path.join("media", "no_picture.jpg")

        # Assert that the file exists in the media folder
        self.assertTrue(os.path.exists(image_path))

        # Generate a unique identifier for the test image file name
        test_image_name = f"test_no_picture_{uuid.uuid4().hex}.jpg"

        # Create a Recipe instance without setting the pic attribute
        recipe = Recipe.objects.get(id=3)
        # Set the pic attribute using the existing "no_picture.jpg" file
        with open(image_path, "rb") as f:
            recipe.pic.save(test_image_name, File(f))

        # Retrieve the Recipe instance and check if the pic attribute is set correctly
        recipe = Recipe.objects.get(id=recipe.id)
        expected_pic_path = os.path.join("recipe", test_image_name)

        # Replace backslashes with forward slashes in the expected path to make it platform-independent
        expected_pic_path = expected_pic_path.replace("\\", "/")

        self.assertEqual(recipe.pic.name, expected_pic_path)


class RecipeFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.form_data_valid = {
            "search_mode": "#1",
            "ingredient_or_recipe": "Recipe Name",
        }
        cls.form_data_invalid = {
            "search_mode": "#4",  # An invalid choice
            "ingredient_or_recipe": "Recipe Name",
        }
        cls.form_data_blank_search_mode = {
            "search_mode": "",  # An empty choice
            "ingredient_or_recipe": "Recipe Name",
        }
        cls.form_data_blank_ingredient = {
            "search_mode": "#3",
            "ingredient_or_recipe": "",  # Blank input for "#3" search mode
        }

    def test_valid_search_mode(self):
        form = RecipeSearchForm(data=self.form_data_valid)
        # verify the form fields values and check for validation errors
        self.assertTrue(
            form.is_valid(), "Form should be valid with a valid search mode"
        )
        self.assertEqual(form.cleaned_data["search_mode"], "#1")
        self.assertEqual(form.cleaned_data["ingredient_or_recipe"], "Recipe Name")

    def test_invalid_search_mode(self):
        form = RecipeSearchForm(data=self.form_data_invalid)
        # verify the form fields values and check for validation errors
        self.assertFalse(form.is_valid())
        self.assertIn("search_mode", form.errors)

    def test_blank_search_mode(self):
        form = RecipeSearchForm(data=self.form_data_blank_search_mode)
        # verify the form fields values and check for validation errors
        self.assertFalse(form.is_valid())
        self.assertIn("search_mode", form.errors)

    def test_blank_ingredient_or_recipe(self):
        form = RecipeSearchForm(data=self.form_data_blank_ingredient)
        # verify the form fields values and check for validation errors
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["search_mode"], "#3")
        self.assertEqual(form.cleaned_data["ingredient_or_recipe"], "")
