from django.db import models

# Create your models here.
class Portal(models.Model):
    nome = models.CharField(max_length=20)
    url = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome

class Job(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    modelo_contratacao = models.CharField(max_length=15)
    senioridade = models.CharField(max_length=20)
    site_busca = models.ForeignKey(Portal, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.titulo
    
