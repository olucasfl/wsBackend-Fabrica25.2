from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import TreinadorForm
from .models import Treinador

class CriarTreinadorView(View):
    template_name = 'home.html'
    form_class = TreinadorForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            treinador = form.save()
            return redirect('treinadores:perfil', treinador_id=treinador.id)
        return render(request, self.template_name, {'form': form})

class ListaTreinadoresView(View):
    template_name = 'lista_treinadores.html'

    def get(self, request):
        treinadores = Treinador.objects.all()
        return render(request, self.template_name, {'treinadores': treinadores})


class PerfilTreinadorView(View):
    template_name = 'perfil.html'

    def get(self, request, treinador_id):
        treinador = get_object_or_404(Treinador, id=treinador_id)
        return render(request, self.template_name, {'treinador': treinador})
    
class DeletarTreinadorView(View):
    def post(self, request, treinador_id):
        treinador = get_object_or_404(Treinador, id=treinador_id)
        treinador.delete()
        return redirect('treinadores:home')