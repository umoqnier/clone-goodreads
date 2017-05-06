from rest_framework import serializers
from .models import Author
from modules.books.serializers import BookNewSerializer


class AuthorSerializer(serializers.ModelSerializer):
    libros = BookNewSerializer(read_only=True, many=True)

    class Meta:
        model = Author
        fields = ("id", "nombre", "apellidos", "biografia", "nacionalidad", "libros")  # Debe llevar el nombre del models.py de libros


