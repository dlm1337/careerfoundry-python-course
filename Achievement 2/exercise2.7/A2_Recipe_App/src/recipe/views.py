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

        for recipe in queryset:
            recipe.title = get_recipe_from_title(recipe.title)

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


class RecipeSearchView(FormView):
    template_name = "recipe/search.html"
    form_class = RecipeSearchForm

    def form_valid(self, form):
        queryset = self.get_queryset(form)

        # Convert the search results (queryset) into a Pandas DataFrame
        data = {
            "Recipe Title": [recipe.title for recipe in queryset],
            "Other Columns": [
                recipe.directions for recipe in queryset
            ],  # Add other columns as needed
        }
        df = pd.DataFrame(data)

        # Store the DataFrame in the context to access it in the template
        self.extra_context = {
            "search_results_df": df.to_html(
                classes="table table-bordered table-hover", index=False
            )
        }

        return self.render_to_response(self.get_context_data())

    def get_queryset(self, form):
        recipe_name = form.cleaned_data.get("ingredient_or_recipe")
        search_mode = form.cleaned_data.get("search_mode")

        if search_mode == "#1" and not self.request.user.is_authenticated:
            return Recipe.objects.none()

        queryset = Recipe.objects.all()

        if search_mode == "#1":
            # Filter recipes by the current user's recipes only
            queryset = queryset.filter(
                user=self.request.user, title__icontains=recipe_name
            )
        elif search_mode == "#2":
            queryset = queryset.filter(title__icontains=recipe_name)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Check if the search results DataFrame is available in the extra context
        if hasattr(self, "extra_context") and "search_results_df" in self.extra_context:
            search_results_df = self.extra_context["search_results_df"]
            context["search_results_df"] = search_results_df

        return context
