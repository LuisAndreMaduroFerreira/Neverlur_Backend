from django.urls import path
from Neverlur_Backend_API.views.model.genre.AllGenreView import list_genres


url_patterns = [
    path('api/genres', list_genres, 'genres')
]
