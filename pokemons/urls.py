from django.urls import path
from .views import CapturarPokemonView

app_name = 'pokemons'

urlpatterns = [
    path('captura/<int:treinador_id>/', CapturarPokemonView.as_view(), name='captura'),
]
