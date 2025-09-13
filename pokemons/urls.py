from django.urls import path
from .views import CapturarPokemonView, DeletarPokemonView, PokemonDetailAPI, PokemonDetailView

app_name = 'pokemons'

urlpatterns = [
    path('captura/<int:treinador_id>/', CapturarPokemonView.as_view(), name='captura'),
    path('<int:treinador_id>/delete/<int:pokemon_id>/', DeletarPokemonView.as_view(), name='delete'),
    path('detalhes/<int:treinador_id>/<str:name>/', PokemonDetailView.as_view(), name='detalhes_pokemon_view'),
    path('detalhes/api/<int:treinador_id>/<str:name>/', PokemonDetailAPI.as_view(), name='detalhes_pokemon_json'),
]
