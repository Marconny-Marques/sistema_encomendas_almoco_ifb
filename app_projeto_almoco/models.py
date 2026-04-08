from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome_usuario = models.CharField(max_length=255) # CharField é mais performático para nomes curtos
    email_usuario = models.EmailField(max_length=255) # EmailField já valida o formato do e-mail institucional dos alunos

    def __str__(self):
        return self.nome_usuario

class Encomenda(models.Model):
    # Relacionamos a encomenda com o seu modelo de Usuario
    aluno = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    
    # Registra o dia e hora exatos do pedido
    data_pedido = models.DateTimeField(auto_now_add=True)
    
    # Campo opcional para observações
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Encomenda de {self.aluno.nome_usuario} em {self.data_pedido}"