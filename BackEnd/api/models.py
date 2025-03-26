from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField() 

def __str__(self):
    return self.nome

class Produto(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=20, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) # Não precisa do '_id', pois no banco já salva com o _id no final de uma FK

def __str__(self):
    return self.nome