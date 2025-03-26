from rest_framework import serializers
from .models import *


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nome', 'descricao')

class ProdutoSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Produto
        fields = ('id', 'nome', 'descricao', 'preco', 'categoria')