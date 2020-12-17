from django.contrib import admin
from django.urls import path
from Neverlur_Backend_API.views.model.genre.AllGenreView import listGenres
from Neverlur_Backend_API.views.dto.genre.GenreNameMatchSuggestionsDTOView import getGenreMatchSuggestions
from Neverlur_Backend_API.views.model.genre.ParticularGenreView import listGenre
from Neverlur_Backend_API.views.model.artist.AllArtistView import listArtists
from Neverlur_Backend_API.views.many2many.portrayal.PortrayalViewSet import listPostrayals
from Neverlur_Backend_API.views.many2many.rendering.RenderingViewSet import listRenderings
from Neverlur_Backend_API.views.model.song.SongViewSet import listSongs
from Neverlur_Backend_API.views.model.album.AlbumViewSet import listAlbums
from Neverlur_Backend_API.views.many2many.feature.FeatureViewSet import listFeatures
from Neverlur_Backend_API.views.dto.album.AlbumSuggestionsViewSet import getAlbumMatchSuggestions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/genres/', listGenres, name='genres'),
    path('api/suggestions/genres/<str:current_string>/', getGenreMatchSuggestions, name='genres'),
    path('api/genres/<int:pk>/', listGenre, name='genre'),
    path('api/artists/', listArtists, name='artists'),
    path('api/portrayals/', listPostrayals, name='portrayals'),
    path('api/renderings/', listRenderings, name='renderings'),
    path('api/songs/', listSongs, name='songs'),
    path('api/albums/', listAlbums, name='albums'),
    path('api/suggestions/albums/<str:current_string>/', getAlbumMatchSuggestions, name='albums'),
    path('api/features/', listFeatures, name='features')

]
