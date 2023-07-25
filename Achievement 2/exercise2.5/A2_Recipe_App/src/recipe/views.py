from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Recipe


# Create your views here.
def recipes_home(request):
    return render(request, "recipe/recipes_home.html")


# Create your views here.
class RecipeListView(ListView):  # class-based view
    model = Recipe  # specify model
    template_name = "recipe/recipe_list.html"  # specify template


class RecipeDetailView(DetailView):  # class-based view
    model = Recipe  # specify model
    template_name = "recipe/recipe_detail.html"  # specify template
