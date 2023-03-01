from django.db import models
from app_images.models import Categorie

class Modele(models.Model):
    id_modele = models.CharField(primary_key=True, max_length=50)
    url_modele = models.CharField(max_length=500, blank=True, null=True)
    nom_modele = models.CharField(max_length=50, blank=True, null=True)
    accuracy = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    recall = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    statut = models.BooleanField(blank=True, null=True)
    date_fin_entrainement = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'modele'

class Detailsmodele(models.Model):
    id_modele = models.OneToOneField('Modele', models.DO_NOTHING, db_column='id_modele', primary_key=True)
    id_categorie = models.ForeignKey(Categorie, models.DO_NOTHING, db_column='id_categorie')

    class Meta:
        managed = True
        db_table = 'detailsmodele'
        unique_together = (('id_modele', 'id_categorie'))
