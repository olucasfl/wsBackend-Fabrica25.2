from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import PokemonSearchForm
from .models import Pokemon
from treinadores.models import Treinador
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
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
    
class DeletarPokemonView(View):
    def post(self, request, treinador_id, pokemon_id):
        pokemon = get_object_or_404(Pokemon, id=pokemon_id, treinador_id=treinador_id)
        pokemon.delete()
        return redirect('treinadores:perfil', treinador_id=treinador_id)
    
class PokemonDetailAPI(APIView):
    def get(self, request, treinador_id, name):
            p = get_object_or_404(Pokemon, treinador_id=treinador_id, nome=name)
            data = {
                "name": p.nome,
                "sprite": p.sprite,
                "types": p.tipos.split(","),
                "stats": p.stats
            }
            return Response(data)
    
class PokemonDetailView(View):
    template_name = 'detalhes_pokemon.html'

    def get(self, request, treinador_id, name):
        treinador = get_object_or_404(Treinador, id=treinador_id)
        pokemon = get_object_or_404(Pokemon, treinador_id=treinador_id, nome=name)
        return render(request, self.template_name, {"pokemon": pokemon, "treinador": treinador})
