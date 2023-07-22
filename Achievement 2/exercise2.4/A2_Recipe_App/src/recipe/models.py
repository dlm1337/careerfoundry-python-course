from django.db import models

RECIPE_TYPES = (
    ("breakfast", "Breakfast"),
    ("lunch", "Lunch"),
    ("dinner", "Dinner"),
    ("appetizer", "Appetizer"),
    ("dessert", "Dessert"),
    ("snack", "Snack"),
    ("drink", "Drink"),
    ("cocktail", "Cocktail"),
    ("other", "Other"),
)


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    user = models.ForeignKey(
        "user.User",
        on_delete=models.CASCADE,
        default=None,
        null=True,
        related_name="recipes",
    )
    recipe_ingredients = models.ManyToManyField(
        "recipeingredient.RecipeIngredient",
        through="recipeingredientintermediary.RecipeIngredientIntermediary",
    )
    directions = models.TextField()
    cooking_time = models.PositiveIntegerField(null=True, blank=False)
    star_count = models.PositiveIntegerField(
        choices=[(i, i) for i in range(1, 6)], null=True, blank=False
    )
    recipe_type = models.CharField(max_length=100, choices=RECIPE_TYPES, blank=False)
    adapted_link = models.URLField(blank=True, null=True, default=None)
    servings = models.PositiveIntegerField(null=True, blank=False)
    yield_amount = models.IntegerField(blank=True, null=True, default=None)
    allergens = models.TextField(blank=True)

    def __str__(self):
        return str(self.title)
