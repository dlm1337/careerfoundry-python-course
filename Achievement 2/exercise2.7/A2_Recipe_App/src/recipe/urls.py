from django.urls import path
from .views import RecipeListView
from .views import RecipeDetailView
from .views import RecipeHome
from .views import RecipeSearchView

app_name = "recipe"


urlpatterns = [
    path("", RecipeHome.as_view(), name="home"),
    path("list/", RecipeListView.as_view(), name="list"),
    path("list/<pk>", RecipeDetailView.as_view(), name="detail"),
    path("search/", RecipeSearchView.as_view(), name="search"),
]
