from django.db import models

class Modele(models.Model):
    id_modele = models.CharField(primary_key=True, max_length=50)
    nom_modele = models.CharField(max_length=50, blank=True, null=True)
    accuracy = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    recall = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    statut = models.BooleanField(blank=True, null=True)
    date_fin_entrainement = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'modele'
