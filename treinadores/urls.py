from django.urls import path
from .views import CriarTreinadorView, PerfilTreinadorView, ListaTreinadoresView, DeletarTreinadorView, AtualizarTreinadorView

app_name = 'treinadores'

urlpatterns = [
    path('', CriarTreinadorView.as_view(), name='home'),
    path('perfil/<int:treinador_id>/', PerfilTreinadorView.as_view(), name='perfil'),
    path('lista/', ListaTreinadoresView.as_view(), name='lista'),
    path('deletar/<int:treinador_id>/', DeletarTreinadorView.as_view(), name='deletar'),
    path('atualizar/<int:treinador_id>/', AtualizarTreinadorView.as_view(), name='atualizar'),
]
