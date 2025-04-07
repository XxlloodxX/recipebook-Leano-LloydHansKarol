from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Ingredient, Recipe, RecipeIngredient, RecipeImage
from .forms import RecipeForm, RecipeIngredientForm, IngredientForm, RecipeImageForm


@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipe': recipes})

@login_required
def recipe_with_param(request, param):
    recipe = Recipe.objects.get(id = param)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)
        
    return render(request, 'recipe_id.html', {'recipe':recipe, 'ingredients':ingredients})

@login_required
def recipe_add(request):
    recipe_form = RecipeForm(request.POST or None)
    ingredient_form = IngredientForm(request.POST or None)
    recipe_ingredient_form = RecipeIngredientForm(request.POST or None)

    if (request.method == 'POST'):
        if 'create_recipe' in request.POST and recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user.profile  
            recipe.save()
            return redirect('ledger:recipe_add')

        elif 'create_ingredient' in request.POST and ingredient_form.is_valid():
            ingredient_form.save() 
            return redirect('ledger:recipe_add')  

        elif 'create_recipe_ingredient' in request.POST and recipe_ingredient_form.is_valid():
            recipe_ingredient_form.save()
            return redirect('ledger:recipe_add')

    return render(request, 'recipe_create.html', {
        'recipe_form': recipe_form,
        'ingredient_form': ingredient_form,
        'recipe_ingredient_form': recipe_ingredient_form,
    })

def recipe_image(request, pk):
    recipe = Recipe.objects.get(id = pk)
    if request.method == 'POST':
        image_form = RecipeImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = image_form.save(commit=False)
            image.recipe = recipe
            image.save()
            return redirect('ledger:recipe_with_param', param=recipe.pk)
    else:
        image_form = RecipeImageForm()
    
    return render(request, 'recipe_add_image.html', {'recipe': recipe, 'image_form': image_form})