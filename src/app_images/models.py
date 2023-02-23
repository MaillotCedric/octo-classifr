from django.db import models

class Categorie(models.Model):
    id_categorie = models.CharField(primary_key=True, max_length=50)
    nom_categorie = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'categorie'

class Image(models.Model):
    url = models.CharField(primary_key=True, max_length=500)
    nom_image = models.CharField(max_length=50, blank=True, null=True)
    id_categorie = models.ForeignKey(Categorie, models.DO_NOTHING, db_column='id_categorie', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'image'
