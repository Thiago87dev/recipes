from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
from django.db.models import Q
from .models import Recipe
from utils.pagination import make_pagination


def home(request):
    recipes = Recipe.objects.all().filter(is_published=True).order_by('-id')

    page_obj, pagination_range = make_pagination(request, recipes, 9)

    return render(request, 'recipes/pages/home.html', {
        'recipes': page_obj,
        'pagination_range': pagination_range
    })


def category(request, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id, is_published=True).order_by('-id'))

    page_obj, pagination_range = make_pagination(request, recipes, 9)

    return render(request, 'recipes/pages/category.html', {
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'title': f'Category | {recipes[0].category.name}'
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id, is_published=True)

    return render(request, 'recipes/pages/recipe-view.html',
                  {
                      'recipe': recipe,
                      'is_detail_page': True
                  })


def search(request):
    search_term = request.GET.get('q', '').strip()

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True
    ).order_by('-id')

    if not search_term:
        raise Http404()

    page_obj, pagination_range = make_pagination(request, recipes, 9)

    return render(request, 'recipes/pages/search.html', {
        'search_term': search_term,
        'page_title': f'Search for "{search_term}"',
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}'
    })
