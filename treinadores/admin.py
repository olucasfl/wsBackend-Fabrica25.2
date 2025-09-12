from django.contrib import admin
from .models import Treinador

@admin.register(Treinador)
class TreinadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'cidade', 'nivel')
    search_fields = ('nome', 'cidade')
