from django.contrib import admin
from .models import *


# class DirectorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug')
#     prepopulated_fields = {'slug': ('name',)}

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'director', 'grade_kinopoisk', 'grade_imdb')
    prepopulated_fields = {'slug': ('name',)}


# admin.site.register(Director, DirectorAdmin)
admin.site.register(Movie, MovieAdmin)

