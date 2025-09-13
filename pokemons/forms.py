from django import forms

class PokemonSearchForm(forms.Form):
    name = forms.CharField(max_length=50)
