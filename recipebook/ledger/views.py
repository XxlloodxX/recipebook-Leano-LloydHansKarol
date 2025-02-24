from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def recipe_list(request):
    template = loader.get_template('recipe_list.html')
    return HttpResponse(template.render())

#def recipe_with_param(request, param="list"):
    #template for recipe 1 & 2