from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Usuario
from django.contrib import messages # Importe messages

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    # Só salva se o método for POST (envio do formulário)
    if request.method == 'POST':
        email_digitado = request.POST.get('email_usuario')

        # Verifica se é um e-mail institucional pela terminação "edu.br"
        if not email_digitado.endswith('edu.br'): 
            messages.error(request, 'Utilize o seu e-mail institucional!')
            return redirect ('home')

        
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

#Confirma o almoço de forma independente do login
def confirmar_almoco(request, id_usuario):
    if request.method == 'POST':
         agora = timezone.localtime(timezone.now())
         limite = agora.replace(hour=9, minute=30, second=0, microsecond=0)

         if agora>limite:
              messages.error(request, 'O horário limite para confirmar o almoço é até às (9:30h)')
              return redirect('home')
         
         pedido = Usuario.objects.get(id_usuario=id_usuario)

         pedido.pedido_confirmado = not pedido.pedido_confirmado
         pedido.save()

    if pedido.pedido_confirmado:
                messages.success(request, 'Pedido confirmado!')
    else:
                messages.warning(request, 'Pedido cancelado!')