from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome_usuario = models.CharField(max_length=255) 
    email_usuario = models.EmailField(max_length=255)
    data_encomenda = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nome_usuario

class Encomenda(models.Model):
    # Relaciona a encomenda com o modelo de Usuario/Aluno
    aluno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    # Registra o dia e hora exatos do pedido
    data_pedido = models.DateTimeField(auto_now_add=True)
    
    # Campo para observações
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Encomenda de {self.aluno.nome_usuario} em {self.data_pedido}"