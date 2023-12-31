import json
from django.views.generic import ListView, DetailView, FormView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeSearchForm
import pandas as pd
from .utils import get_recipe_from_title, get_chart
from django.shortcuts import redirect, render
from django.utils.html import format_html


class RecipeHome(ListView):
    model = Recipe
    template_name = "recipe/recipes_home.html"

    def get_queryset(self):
        queryset = super().get_queryset()

        for recipe in queryset:
            recipe.title = get_recipe_from_title(recipe.title)

        return queryset


class YourRecipesView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipe/your_recipes.html"

    def get_queryset(self):
        ## function get_queryset is automatically called by ListView and get the request
        # user and filters recipes by username.
        user = self.request.user
        queryset = Recipe.objects.filter(user=user)

        return queryset


def format_cost(cost):
    return f"${cost:.2f}"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe/recipe_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Extract ingredient names from the RecipeIngredient objects
        ingredients = [
            ing.ingredient.name for ing in context["object"].recipe_ingredients.all()
        ]

        # Create a dictionary with ingredient names as keys
        ingredient_data = {ingredient: None for ingredient in ingredients}

        df = pd.DataFrame.from_dict(
            ingredient_data, orient="index", columns=["Calorie Content"]
        )

        # Set the 'Calorie Content', 'Grams' and 'Cost' for each ingredient
        for ing in context["object"].recipe_ingredients.all():
            df.loc[ing.ingredient.name, "Calorie Content"] = ing.calorie_content
            df.loc[ing.ingredient.name, "Grams"] = ing.grams
            df.loc[ing.ingredient.name, "Cost"] = format_cost(float(ing.cost))

        # Convert the DataFrame to HTML
        df_html = df.to_html(classes="table table-bordered table-hover", escape=False)

        # Manually add the table ID to the generated HTML
        df_html = df_html.replace("<table", '<table id="ingredient-info-table"')
        context["recipe_dataframe"] = df_html

        # Get the chart HTML using the get_chart
        chart1 = get_chart("#1", df, x=df.index, y="Calorie Content")
        chart2 = get_chart("#2", df, x=df.index, y="Grams")
        chart3 = get_chart("#3", df, x=df.index, y="Cost")

        context["chart1"] = chart1
        context["chart2"] = chart2
        context["chart3"] = chart3

        return context


class RecipeSearchView(FormView):
    template_name = "recipe/search.html"
    form_class = RecipeSearchForm

    def form_valid(self, form):
        queryset = self.get_queryset(form)

        # Create a dictionary to store recipe titles and their absolute URLs
        recipe_urls = {recipe.title: recipe.get_absolute_url() for recipe in queryset}
        # Convert the recipe_urls dictionary to a JSON string
        recipe_urls_json = json.dumps(recipe_urls)

        # Convert the queryset to a DataFrame
        data = {
            "Recipe Title": [recipe.title for recipe in queryset],
            "Star Count": [recipe.star_count for recipe in queryset],
            "Cooking Time": [recipe.cooking_time for recipe in queryset],
            "Picture": [recipe.pic.url for recipe in queryset],
        }
        df = pd.DataFrame(data)

        # Modify the DataFrame to include the image as an HTML img tag
        df["Picture"] = df["Picture"].apply(
            lambda url: format_html('<img src="{}" width="200px">', url)
        )

        # Convert the modified DataFrame to HTML
        search_results_df = df.to_html(
            classes="table table-bordered table-hover", index=False, escape=False
        )
        # Manually add the table ID to the generated HTML
        search_results_df = search_results_df.replace(
            "<table", '<table id="search-results-table"'
        )

        context = {
            "search_results_df": search_results_df,
            "recipe_urls_json": recipe_urls_json,
        }

        return render(self.request, self.template_name, context)

    def get_queryset(self, form):
        search = form.cleaned_data.get("search")
        search_mode = form.cleaned_data.get("search_mode")

        if search_mode == "#1" and not self.request.user.is_authenticated:
            return Recipe.objects.none()

        queryset = Recipe.objects.all()

        if search_mode == "#1":
            # Filter recipes by the current user's recipes only
            queryset = Recipe.objects.filter(
                user=self.request.user, title__icontains=search
            )
            if search.strip():
                if not queryset.exists():
                    # Filter recipes by the ingredient name
                    queryset = Recipe.objects.filter(
                        user=self.request.user,
                        recipe_ingredients__ingredient__name__icontains=search,
                    )
            else:
                queryset = Recipe.objects.none()

        elif search_mode == "#2":
            # Only filter if the search bar is not blank
            if search.strip():
                queryset = Recipe.objects.filter(title__icontains=search)
                if not queryset.exists():
                    # Filter recipes by the ingredient name
                    queryset = Recipe.objects.filter(
                        recipe_ingredients__ingredient__name__icontains=search
                    )
            else:
                queryset = Recipe.objects.none()

        elif search_mode == "#3":
            queryset = Recipe.objects.all()

        return queryset
