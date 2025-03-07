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
    RecipeIngredient.objects.create(quantity = "3pcs", ingredients = Ingredient.objects.get(name="tomato"), recipe = Recipe.objects.get(name="Recipe 1"))
    RecipeIngredient.objects.create(quantity = "1pc", ingredients = Ingredient.objects.get(name="onion"), recipe = Recipe.objects.get(name="Recipe 1"))
    RecipeIngredient.objects.create(quantity = "1kg", ingredients = Ingredient.objects.get(name="pork"), recipe = Recipe.objects.get(name="Recipe 1"))
    RecipeIngredient.objects.create(quantity = "1L", ingredients = Ingredient.objects.get(name="water"), recipe = Recipe.objects.get(name="Recipe 1"))
    RecipeIngredient.objects.create(quantity = "1 packet", ingredients = Ingredient.objects.get(name="sinigang mix"), recipe = Recipe.objects.get(name="Recipe 1"))
    
    RecipeIngredient.objects.create(quantity = "1 head", ingredients = Ingredient.objects.get(name="garlic"), recipe = Recipe.objects.get(name="Recipe 2"))
    RecipeIngredient.objects.create(quantity = "1 pc", ingredients = Ingredient.objects.get(name="onion"), recipe = Recipe.objects.get(name="Recipe 2"))
    RecipeIngredient.objects.create(quantity = "1/2cup", ingredients = Ingredient.objects.get(name="vinegar"), recipe = Recipe.objects.get(name="Recipe 2"))
    RecipeIngredient.objects.create(quantity = "1 cup", ingredients = Ingredient.objects.get(name="water"), recipe = Recipe.objects.get(name="Recipe 2"))
    RecipeIngredient.objects.create(quantity = "1 tablespoon", ingredients = Ingredient.objects.get(name="salt"), recipe = Recipe.objects.get(name="Recipe 2"))
    RecipeIngredient.objects.create(quantity = "1 tablespoon", ingredients = Ingredient.objects.get(name="whole black peppers"), recipe = Recipe.objects.get(name="Recipe 2"))
    RecipeIngredient.objects.create(quantity = "1 kilo", ingredients = Ingredient.objects.get(name="pork"), recipe = Recipe.objects.get(name="Recipe 2"))

    return HttpResponse("Added Recipes and Ingredients")