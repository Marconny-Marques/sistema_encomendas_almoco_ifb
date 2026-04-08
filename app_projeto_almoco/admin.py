from django.contrib import admin
from .models import Encomenda

@admin.register(Encomenda)
class EncomendaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'data_pedido', 'observacoes')
    list_filter = ('data_pedido',) # Permite filtrar por data na lateral
    search_fields = ('aluno__username', 'aluno__first_name') # Permite buscar pelo nome do aluno