from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True, null=True, blank=True)

class RecipeImage(models.Model):
    image = models.ImageField(upload_to='recipe_images/', null=False)
    description = models.CharField(max_length=255, blank=True)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='images')

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredients = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name="recipe")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")