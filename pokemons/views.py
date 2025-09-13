from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import PokemonSearchForm
from .models import Pokemon
from treinadores.models import Treinador
import requests

class CapturarPokemonView(View):
    template_name = 'capturar_pokemon.html'

    def get(self, request, treinador_id):
        form = PokemonSearchForm()
        treinador = get_object_or_404(Treinador, id=treinador_id)
        return render(request, self.template_name, {"form": form, "treinador": treinador})

    def post(self, request, treinador_id):
        form = PokemonSearchForm(request.POST)
        treinador = get_object_or_404(Treinador, id=treinador_id)
        context = {"form": form, "treinador": treinador}

        if form.is_valid():
            name = form.cleaned_data["name"].lower()
            response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}/')

            if response.status_code == 200:
                data = response.json()
                pokemon, created = Pokemon.objects.update_or_create(
                    treinador=treinador,
                    nome=data["name"],
                    defaults={
                        "sprite": data["sprites"]["front_default"],
                        "tipos": ",".join([t["type"]["name"] for t in data["types"]]),
                        "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}
                    }
                )
                context["success"] = True
                context["pokemon"] = pokemon
            else:
                context["error"] = f"Não foi possível capturar '{name.capitalize()}'. Pokémon não encontrado."

        return render(request, self.template_name, context)
