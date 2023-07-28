from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin


class RecipeHome(ListView):
    model = Recipe
    template_name = "recipe/recipes_home.html"


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
