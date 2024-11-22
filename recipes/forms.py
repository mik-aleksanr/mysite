from .models import Recipe
from django.forms import ModelForm, TextInput, Textarea, ImageField, NumberInput
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'preparation_steps', 'preparation_time', 'image', 'categories', 'author']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Название рецепта "
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Описание рецепта"
            }),
            'preparation_steps': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Приготовление"
            }),
            'preparation_time': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Время приготовления"
            }),
            'categories': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Категория блюда"
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Имя автора"
            }),

        }


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
