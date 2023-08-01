from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RecipeSearchForm

import pandas as pd
from .utils import get_recipe_from_title


class RecipeHome(ListView):
    model = Recipe
    template_name = "recipe/recipes_home.html"

    def get_queryset(self):
        # Access the request object using self.request
        # Example: accessing query parameters
        form = RecipeSearchForm(self.request.POST or None)
        sales_df = None  # initialize dataframe to None 
        # check if the button is clicked
        if self.request.method == "POST":
            # read book_title and chart_type
            recipe = self.request.POST.get("ingredient_or_recipe")
            search_mode = self.request.POST.get("search_mode")

            # apply filter to extract data
            qs = Recipe.objects.filter(title=recipe)
            if qs:  # if data found
                # convert the queryset values to pandas dataframe
                sales_df = pd.DataFrame(qs.values())
                # convert the ID to Name of book
                sales_df["recipe_title"] = sales_df["recipe_title"].apply(
                    get_recipe_from_title
                )

                sales_df = sales_df.to_html()

        # Modify the queryset based on the request, if needed
        queryset = super().get_queryset()
        # Additional queryset filtering or processing based on the request

        return queryset


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipe/recipe_list.html"

    def get_queryset(self):
        ## function get_queryset is automatically called by ListView and get the request
        # user and filters recipes by username.
        user = self.request.user
        queryset = Recipe.objects.filter(user=user)

        return queryset


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipe/recipe_detail.html"
