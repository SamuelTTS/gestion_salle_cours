from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Salle(models.Model):
    numero = models.CharField(max_length=50)
    capacite = models.IntegerField(default=0)
    disponible = models.BooleanField(default=True)

class Reservation(models.Model):
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    professeur = models.CharField(max_length=100)
    matiere = models.CharField(max_length=100)
    terminee=models.BooleanField(default=False)