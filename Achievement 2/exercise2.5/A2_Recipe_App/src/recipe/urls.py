from django.urls import path
from .views import RecipeListView
from .views import RecipeDetailView
from .views import RecipeHome

app_name = "recipe"


urlpatterns = [
    path("", RecipeHome.as_view(), name="home"),
    path("list/", RecipeListView.as_view(), name="list"),
    # Other URL patterns for different views can go here if you have any.
    path("list/<pk>", RecipeDetailView.as_view(), name="detail"),
]
