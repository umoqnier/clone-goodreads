from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):

    author_name = serializers.CharField(source="autor.nombre")
    author_lastname = serializers.CharField(source="autor.apellido")  # Solucionando tablas con llaves foraneas

    class Meta:
        model = Book
        # exclude = ("rating", )  # Quitando rating
        fields = ('id', 'nombre', 'descripcion', 'ISBN', 'author_name', 'author_lastname')