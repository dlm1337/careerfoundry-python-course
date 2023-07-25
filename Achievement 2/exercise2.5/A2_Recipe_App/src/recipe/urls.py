from django.urls import path
from .views import recipes_home

from .views import RecipeListView 
from .views import RecipeDetailView

app_name = "recipe"


urlpatterns = [
    path("", recipes_home),
    
    path('list/', RecipeListView.as_view(), name='list'),
    # Other URL patterns for different views can go here if you have any.
    path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
]
