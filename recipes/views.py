from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes/index.html'
    context_object_name = 'recipes'
    queryset = Recipe.objects.order_by('?')[:5]


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes/recipe_detail.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user.username
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.object.pk})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("recipes:index")
    else:
        form = RegistrationForm()
    return render(request, "recipes/register.html", {"form": form})
