from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Ingredient, Recipe, RecipeIngredient

# Create your views here.
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipe': recipes})

def recipe_with_param(request, param):
    recipe = Recipe.objects.get(id = param)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)
        
    return render(request, 'recipe_id.html', {'recipe':recipe, 'ingredients':ingredients})