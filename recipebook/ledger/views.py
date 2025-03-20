from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Ingredient, Recipe, RecipeIngredient

# Create your views here.
@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipe': recipes})

@login_required
def recipe_with_param(request, param):
    recipe = Recipe.objects.get(id = param)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)
        
    return render(request, 'recipe_id.html', {'recipe':recipe, 'ingredients':ingredients})