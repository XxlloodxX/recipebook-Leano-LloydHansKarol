from django.urls import path
from . import views
from django.shortcuts import redirect
from .views import recipe_list, recipe_with_param

urlpatterns = [
    path('', lambda request: redirect('ledger:recipe_list'), name="home"),
    path('recipes/list', recipe_list, name="recipe_list"),
    path('recipe/<int:param>', recipe_with_param, name="recipe_with_param"),
    ]

app_name = "ledger"