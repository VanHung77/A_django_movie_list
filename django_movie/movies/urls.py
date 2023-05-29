from django.urls import path

from . import views
from .views import SearchMovieListView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.MoviesView.as_view(), name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),

    path('search/', views.SearchMovieListView.as_view(), name='search_movies'),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
    
    # path("<int:pk>/", views.MovieDetailView.as_view()),
    #path("filter/", views.FilterMoviesView.as_view(), name='filter'),
    #path("search/", views.Search.as_view(), name='search'),
    #path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    #path("json-filter/", views.JsonFilterMoviesView.as_view(), name='json_filter'),
    #path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    #path("actor/<str:slug>/", views.ActorView.as_view(), name="actor_detail"),
]
