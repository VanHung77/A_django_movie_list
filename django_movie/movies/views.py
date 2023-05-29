from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from movies.models import Movie


class MoviesView(ListView):
    """Movie List"""
    model = Movie
    paginate_by = 15
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """Movie Detail"""
    model = Movie
    slug_field = "url"
    

class SearchMovieListView(ListView):
    model = Movie

    def get_queryset(self):
        query = self.request.GET.get('query', '')
        return Movie.objects.filter(
            Q(title__icontains=query) | Q(actors__icontains=query)
        )

class CustomLoginView(LoginView):
    template_name = 'movies/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

class RegisterPage(FormView): 
    template_name = 'movies/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)