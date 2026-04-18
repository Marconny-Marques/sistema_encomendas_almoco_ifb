from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Usuario
from django.contrib import messages # Importe messages


def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    # Só salva se o método for POST (envio do formulário)
    if request.method == 'POST':
        agora = timezone.localtime(timezone.now())
        limite = agora.replace(hour=9, minute=30, second=0, microsecond=0)

        if agora > limite:
            messages.error(request, 'O horário limite para encomendas é até às (9:30) já expirou!')
            return redirect('quantidade_encomendas')
        
        novo_usuario = Usuario()
        novo_usuario.nome_usuario = request.POST.get('nome_usuario')
        novo_usuario.email_usuario = request.POST.get('email_usuario')
        novo_usuario.save()

        messages.success(request, 'Encomenda realizada com sucesso!')


    context = {
        'usuarios' : Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', context)

