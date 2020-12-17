from django.urls import path
from Neverlur_Backend_API.views.dto.genre.GenreNameAutoCompleteSuggestionDTOView import get_suggestions


url_patterns = [
    path('api/suggestions/genres', get_suggestions, 'genres')
]
