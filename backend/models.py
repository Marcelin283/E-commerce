from django.db import models
from datetime import date

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length = 100)

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()
    categorie = models.CharField(max_length = 100)
    qte = models.IntegerField()

class Vente(models.Model):
    produit = models.ForeignKey(Produit, on_delete = models.CASCADE)
    quantite = models.IntegerField()
    date = models.DateField()

class Numero(models.Model):
    numero = models.CharField(max_length=20)