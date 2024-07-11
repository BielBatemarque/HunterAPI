from django.db import models

# Create your models here.
class Job(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    modelo_contratacao = models.CharField(max_length=15)
    senioridade = models.CharField(max_length=20)
    site_busca = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.titulo
    

class Portal(models.Model):
    nome = models.CharField(max_length=20)
    url = models.CharField(max_length=100)