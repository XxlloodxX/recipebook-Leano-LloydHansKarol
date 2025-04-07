from django.urls import path
from . import views
from django.shortcuts import redirect
from .views import recipe_list, recipe_with_param, recipe_add, recipe_image

urlpatterns = [
    path('', lambda request: redirect('ledger:recipe_list'), name="home"),
    path('recipes/list', recipe_list, name="recipe_list"),
    path('recipe/<int:param>', recipe_with_param, name="recipe_with_param"),
    path('recipe/add/', recipe_add, name="recipe_add"),
    path('recipe/<int:pk>/add_image', recipe_image, name="recipe_image"),
    ]

app_name = "ledger"