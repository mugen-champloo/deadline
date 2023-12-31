from django.db import models
from django.urls import reverse


class Director(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Режисер')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('director', kwargs={'director_slug': self.slug})

class Genre(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Жанр")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('genre', kwargs={'genre_slug': self.slug})
    
class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", null=True)
    year = models.IntegerField(blank=True)
    image = models.ImageField(null=True, blank=True)
    info = models.TextField(blank=True, verbose_name='Инфо')
    grade_kinopoisk = models.FloatField(blank=True)
    grade_imdb = models.FloatField(blank=True)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('watch', kwargs={'product_slug': self.slug})
 
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.movie
    
class MovieDirector(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True)
   
    def __str__(self):
        return self.name
    
