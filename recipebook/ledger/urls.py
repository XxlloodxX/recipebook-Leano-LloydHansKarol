from django.urls import path
from . import views
from .views import recipe_list, recipe_with_param

urlpatterns = [
    path('recipes/list', recipe_list, name="recipe_list"),
    path('recipe/<param>', recipe_with_param, name="recipe_with_param"),
    ]

app_name = "ledger"