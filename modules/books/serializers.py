from rest_framework import serializers
from .models import Book, Comments
# from modules.authors.serializers import AuthorSerializer
from modules.users.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comments
        fields = ('user', 'comentario')


class BookSerializer(serializers.ModelSerializer):
    # author_name = serializers.CharField(source="autor.nombre")
    # author_lastname = serializers.CharField(source="autor.apellido")  # Solucionando tablas con llaves foraneas
    # autor = AuthorSerializer(read_only=True)  # Debe llamarse igual que el models.py de author
    comentarios = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        # exclude = ("rating", )  # Quitando rating
        fields = ('id', 'nombre', 'descripcion', 'ISBN', 'comentarios')


class BookNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
