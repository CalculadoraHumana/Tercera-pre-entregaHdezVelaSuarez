from django.db import models

class MiModelo(models.Model):
    campo1 = models.CharField(max_length=50)
    campo2 = models.IntegerField(default=0)
    campo3 = models.DateField()

class SegundoModelo(models.Model):
    campo4 = models.CharField(max_length=100)
    campo5 = models.IntegerField(default=0)
    campo6 = models.DateField()

class TercerModelo(models.Model):
    campo7 = models.CharField(max_length=200)
    campo8 = models.TextField()
    campo9 = models.DateTimeField(auto_now_add=True)

# Create your models here.
