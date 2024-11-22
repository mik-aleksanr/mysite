from django.urls import path
from . import views
from .views import RecipeListView, RecipeDetailView, RecipeCreateView

app_name = 'recipes'

urlpatterns = [
    path('', RecipeListView.as_view(), name='index'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='detail'),
    path('recipe/add/', RecipeCreateView.as_view(), name='add'),
    path("register/", views.register, name="register"),
]
