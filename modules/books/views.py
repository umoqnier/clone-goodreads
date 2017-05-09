from django.shortcuts import render
from rest_framework import generics, filters
from .models import Book
from .serializers import BookSerializer
from .serializers import BookNewSerializer
import django_filters.rest_framework
from rest_framework.permissions import IsAuthenticated


class ListBook(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend, )
    filter_fields = ('nombre', 'ISBN', 'autor', 'genero_literario')  # como filtrar datos
    search_fields = ('nombre', 'ISBN', 'descripcion')  # cómo buscamos datos


class DetailBook(generics.RetrieveDestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
