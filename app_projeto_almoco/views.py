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

        email_digitado = request.POST.get('email_usuario')

        # Verifica se é um e-mail institucional pela terminação "edu.br"
        if not email_digitado.endswith('edu.br'): 
            messages.error(request, 'utilize o seu e-mail institucional!')
            return redirect ('home')


        if agora > limite:
            messages.error(request, 'O horário limite para encomendas é até às (9:30h) já expirou!')
            return redirect('home')
        
        ja_encomendou = Usuario.objects.filter(
            email_usuario = email_digitado,
            data_encomenda = agora.date()
        ).exists()

        if ja_encomendou:
            messages.error(request, "Você já realizou uma encomenda. O limite é uma por dia!")
            return redirect('home')
        
        novo_usuario = Usuario()
        novo_usuario.nome_usuario = request.POST.get('nome_usuario')
        novo_usuario.email_usuario = request.POST.get('email_usuario')
        novo_usuario.save()

        messages.success(request, 'Encomenda realizada com sucesso!')
        return redirect('home')


    context = {
        'usuarios' : Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', context)

