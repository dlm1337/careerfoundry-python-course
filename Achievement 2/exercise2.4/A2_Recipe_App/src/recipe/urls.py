from django.urls import path
from .views import recipes_home

app_name = "recipe"


urlpatterns = [
    path("", recipes_home),
]
