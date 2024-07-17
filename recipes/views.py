from django.shortcuts import render


def teste(request):
    return render(request, 'recipes/pages/home.html')
