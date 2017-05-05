from django.db import models


class Author(models.Model):
    GENEROS = (
        ("DR", "Drama"),
        ("CM", "Comedia"),
        ("FT", "Fantasia"),
        ("CF", "Ciencia Ficción"),
        ("PS", "Poesia"),
        ("LC", "Literatura Contemporanea"),
        ("LH", "Literatura Hispana"),
        ("LU", "Literatura Universal"),
        ("HS", "Historica")
    )
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    biografia = models.TextField()
    sexo = models.CharField(choices=(('M', 'Mujer'), ('H', 'Hombre')), max_length=16)
    genero_literario = models.CharField(choices=GENEROS, max_length=50)
    edad = models.IntegerField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "Autor: %s %s " % (self.nombre, self.apellidos)

