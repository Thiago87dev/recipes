from django.urls import path
from recipes.views import teste

urlpatterns = [
    path('', teste),
]
