from django import forms
from .models import Treinador

class TreinadorForm(forms.ModelForm):
    class Meta:
        model = Treinador
        fields = ['nome', 'idade', 'cidade']

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if Treinador.objects.filter(nome=nome).exists():
            raise forms.ValidationError("Já existe um treinador com esse nome.")
        return nome