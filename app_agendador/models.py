from django.db import models
import datetime

# Create your models here.

class Agenda(models.Model):
    nome = models.CharField(max_length=50)
    dt_criacao = models.DateTimeField(auto_now_add=True)
    dt_audiencia = models.DateField()

    lista_responsaveis = (
        ("Brendon", "Brendon"),
        ("Raphaela", "Raphaela"),
    )
    responsavel = models.CharField(max_length=50, choices=lista_responsaveis)

    lista_classes = (
        ("Trabalhista", "Trabalhista"),
        ("Penal", "Penal"),
        ("Civil", "Civil"),
    )

    classe = models.CharField(max_length=50, choices=lista_classes)

    def __str__(self):
        return self.nome
