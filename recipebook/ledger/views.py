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

def recipe_populate(request):
    Recipe.objects.create(name = "Recipe 1")
    Recipe.objects.create(name = "Recipe 2")

    Ingredient.objects.create(name = "tomato")
    Ingredient.objects.create(name = "onion")
    Ingredient.objects.create(name = "pork")
    Ingredient.objects.create(name = "water")
    Ingredient.objects.create(name = "sinigang mix")
    
    Ingredient.objects.create(name = "garlic")
    Ingredient.objects.create(name = "vinegar")
    Ingredient.objects.create(name = "salt")
    Ingredient.objects.create(name = "whole black peppers")

    return HttpResponse("Added Recipes and Ingredients")