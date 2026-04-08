from django.urls import path
from app_projeto_almoco import views

urlpatterns = [
    # rota, view responsável, nome de referêncio
    #usuarios.com
    path('',views.home,name='home'),

    path('usuarios/',views.usuarios,name='quantidade_encomendas')
]
