from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.models import User
from .models import Recipe, Ingredient, RecipeIngredient, Profile, RecipeImage


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ('name',)
    inlines = [RecipeImageInline]

class RecipeImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'description', 'recipe')

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ('name',)

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    list_display = ('quantity',)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(UserAdmin):
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(RecipeImage, RecipeImageAdmin)