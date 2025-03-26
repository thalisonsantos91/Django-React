from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.response import Response
from .models import *

def home(request):
    return HttpResponse("This is the homepage")


class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        categoria = self.queryset.get(pk=pk)    
        serializer = self.serializer_class(categoria)
        return Response(serializer.data)

    def update(self, request, pk=None):
        categoria = self.queryset.get(pk=pk)
        serializer = self.serializer_class(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        categoria = self.queryset.get(pk=pk)  
        categoria.delete()
        return Response(status=204)




class ProdutoViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        produto = self.queryset.get(pk=pk)    
        serializer = self.serializer_class(produto)
        return Response(serializer.data)

    def update(self, request, pk=None):
        produto = self.queryset.get(pk=pk)
        serializer = self.serializer_class(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        produto = self.queryset.get(pk=pk)  
        produto.delete()
        return Response(status=204)