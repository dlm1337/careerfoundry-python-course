from collections import OrderedDict
from django import forms  # import django forms

from django.forms import formset_factory
from recipeingredientintermediary.models import RecipeIngredientIntermediary
from django.forms import BaseInlineFormSet
from .models import Recipe
from recipeingredient.models import RecipeIngredient
from ingredient.models import Ingredient
from django.forms import modelformset_factory
from django.forms import inlineformset_factory

SEARCH__CHOICES = (  # specify choices as a tuple
    (
        "#1",
        "Search by Your Recipes",
    ),
    ("#2", "Search by All Recipes"),
    ("#3", "Show All Recipes"),
)


class RecipeSearchForm(forms.Form):
    search_mode = forms.ChoiceField(choices=SEARCH__CHOICES)
    search = forms.CharField(max_length=150, required=False)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = [
            "user",
            "recipe_ingredients",
        ]  # Exclude user and recipe_ingredient fields from the form

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance


class RecipeIngredientIntermediaryForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredientIntermediary
        fields = ["recipe", "recipe_ingredient"]
