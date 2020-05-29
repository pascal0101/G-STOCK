from django.db import models
from django.utils import timezone

# Create your models here.
class Categorie(models.Model):
    libelle = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now,blank=True,null=True)
    updated_at = models.DateTimeField(default=timezone.now,blank=True,null=True)
    def __str__(self):
        return self.libelle

class Produit(models.Model):
    nom_produit = models.CharField(max_length=255)
    prix_unit = models.FloatField()
    quantite = models.FloatField()
    nom_four = models.CharField(max_length=255)
    contact_four = models.CharField(max_length=255)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE,blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now,blank=True,null=True)
    updated_at = models.DateTimeField(default=timezone.now,blank=True,null=True)
    

class Vente(models.Model):
    quantite = models.FloatField()
    produit = models.ForeignKey(Produit,on_delete=models.CASCADE,blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now,blank=True,null=True)
    updated_at = models.DateTimeField(default=timezone.now,blank=True,null=True)
    