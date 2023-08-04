from django.urls import path
from .views import YourRecipesView
from .views import RecipeDetailView
from .views import RecipeHome
from .views import RecipeSearchView

app_name = "recipe"


urlpatterns = [
    path("", RecipeHome.as_view(), name="home"),
    path("your_recipes/", YourRecipesView.as_view(), name="your_recipes"),
    path("detail/<pk>", RecipeDetailView.as_view(), name="detail"),
    path("search/", RecipeSearchView.as_view(), name="search"),
]
