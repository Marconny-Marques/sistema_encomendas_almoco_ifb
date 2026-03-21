from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    # Só salva se o método for POST (envio do formulário)
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome_usuario = request.POST.get('nome_usuario')
        novo_usuario.email_usuario = request.POST.get('email_usuario')
        novo_usuario.save()

    # Recupera todos os usuários independente de ser POST ou GET
    usuarios_list = {
        'usuarios': Usuario.objects.all()
    }

    #Agora é só retornar os dados para a pagina de listagem de encomendas
    return render(request,'usuarios/usuarios.html',usuarios_list)