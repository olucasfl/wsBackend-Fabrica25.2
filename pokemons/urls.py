from django.urls import path
from .views import CapturarPokemonView, DeletarPokemonView

app_name = 'pokemons'

urlpatterns = [
    path('captura/<int:treinador_id>/', CapturarPokemonView.as_view(), name='captura'),
    path('<int:treinador_id>/delete/<int:pokemon_id>/', DeletarPokemonView.as_view(), name='delete'),
]
