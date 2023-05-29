from django.db import models
from datetime import date

from django.urls import reverse


class Category(models.Model):
    """Category"""
    name = models.CharField("Category", max_length=150)
    description = models.TextField("Category")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Category"


class Actor(models.Model):
    """Actor"""
    name = models.CharField("Name", max_length=100)
    age = models.PositiveSmallIntegerField("Age", default=0)
    description = models.TextField("Description")
    image = models.ImageField("Image", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Аctor"
        verbose_name_plural = "Actor"


class Genre(models.Model):
    """Genre"""
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genre"


class Movie(models.Model):
    """Movie"""
    title = models.CharField("Title", max_length=100)
    tagline = models.CharField("Tagline", max_length=100, default='')
    description = models.TextField("Description")
    poster = models.URLField("Poster", max_length=200, default="")
    year = models.PositiveSmallIntegerField("Year", default=2019)
    country = models.CharField("Country", max_length=30)
    directors = models.CharField(verbose_name="Directors", max_length=100, default="")
    actors = models.CharField(verbose_name="Actors", max_length=100, default="")
    genres = models.CharField(verbose_name="Genres", max_length=100, default="")
    world_premiere = models.DateField("World premiere", default=date.today)
    budget = models.CharField("Budget", max_length=100, default="", help_text="enter the dollar amount")
    fees_in_usa = models.CharField(
        "US Grossing", max_length=100, default="", help_text="enter the dollar amount"
    )
    fees_in_world = models.CharField(
        "World Grossing", max_length=100, default="", help_text="enter the dollar amount"
    )
    category = models.ForeignKey(
        Category, verbose_name="Category", on_delete=models.SET_NULL, null=True
    )
    # trailer_urls = models.CharField("Trailer", max_length=100, default="")
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Draft", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


# class MovieShots(models.Model):
    
#     title = models.CharField("Title", max_length=100)
#     description = models.TextField("Description")
#     image = models.ImageField("Image", upload_to="movie_shots/")
#     movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE, default="")

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = "Film frame"
#         verbose_name_plural = "Film Images"


# class RatingStar(models.Model):
#     """Star rating"""
#     value = models.SmallIntegerField("Value", default=0)

#     def __str__(self):
#         return self.value

#     class Meta:
#         verbose_name = "Star rating"
#         verbose_name_plural = "Stars rating"


# class Rating(models.Model):
#     """Rating"""
#     ip = models.CharField("IP address", max_length=15)
#     star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Star")
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Movie", default="")

#     def __str__(self):
#         return f"{self.star - self.movie}"

#     class Meta:
#         verbose_name = "Rating"
#         verbose_name_plural = "Ratings"

# class Rewiews(models.Model):
#     """Reviews"""
#     email = models.EmailField()
#     name = models.CharField("Name", max_length=100)
#     text = models.TextField("Message", max_length=5000)
#     parent = models.ForeignKey(
#         'self', verbose_name="Parent", on_delete=models.SET_NULL, blank=True, null=True
#     )
#     movie = models.ForeignKey(Movie, verbose_name="Movie", on_delete=models.CASCADE, default="")

#     def __str__(self):
#         return f"{self.name - self.movie}"

#     class Meta:
#         verbose_name = "Reviews"
#         verbose_name_plural = "Reviews"
