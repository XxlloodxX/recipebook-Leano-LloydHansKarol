from django.urls import path
from . import views
from .views import recipe_list, recipe_with_param, recipe_populate

urlpatterns = [
    path('recipes/list', recipe_list, name="recipe_list"),
    path('recipe/<int:param>', recipe_with_param, name="recipe_with_param"),
    path('recipes/populate', recipe_populate, name="recipe_populate"),
    ]

app_name = "ledger"