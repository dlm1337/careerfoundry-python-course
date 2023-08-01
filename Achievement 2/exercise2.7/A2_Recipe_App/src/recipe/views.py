from django.views.generic import ListView, DetailView, FormView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeSearchForm
import pandas as pd
from .utils import get_recipe_from_title
from django.shortcuts import redirect


class RecipeHome(ListView, FormView):
    model = Recipe
    template_name = "recipe/recipes_home.html"
    context_object_name = "recipes"
    form_class = RecipeSearchForm
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            search_mode = form.cleaned_data.get("search_mode")

            if search_mode == "#1" and not request.user.is_authenticated:
                return redirect("login")

        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        form = self.get_form()

        if form.is_valid():
            recipe_name = form.cleaned_data.get("ingredient_or_recipe")
            search_mode = form.cleaned_data.get("search_mode")

            if search_mode == "#1":
                # Filter recipes by the current user's recipes only
                queryset = queryset.filter(
                    user=self.request.user, title__icontains=recipe_name
                )
            elif search_mode == "#2":
                queryset = queryset.filter(title__icontains=recipe_name)
            elif search_mode == "#3":
                # Show all recipes from all users
                queryset = Recipe.objects.all()

        for recipe in queryset:
            recipe.title = get_recipe_from_title(recipe.title)

        return queryset

    def form_valid(self, form):
        return self.get(self.request)  # Refresh the page after form submission


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
