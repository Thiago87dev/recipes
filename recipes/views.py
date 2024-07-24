from django.shortcuts import render
# from utils.factory import make_recipe
from .models import Recipe


def home(request):
    recipes = Recipe.objects.all().filter(is_published=True).order_by('-id')
    # [make_recipe() for _ in range(10)]
    return render(request, 'recipes/pages/home.html', {'recipes': recipes})


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id, is_published=True).order_by('-id')
    # [make_recipe() for _ in range(10)]
    return render(request, 'recipes/pages/category.html', {'recipes': recipes})


def recipe(request, id):
    recipe = Recipe.objects.filter(id=id, is_published=True).first()
    return render(request, 'recipes/pages/recipe-view.html',
                  {
                      #   make_recipe(),
                      'recipe': recipe,
                      'is_detail_page': True
                  })
