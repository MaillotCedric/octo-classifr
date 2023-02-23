from django.db import models
from modeles.models import Modele
from app_images.models import Image

class Prediction(models.Model):
    id_prediction = models.CharField(primary_key=True, max_length=50)
    etat = models.BooleanField(blank=True, null=True)
    commentaire = models.CharField(max_length=200, blank=True, null=True)
    id_modele = models.ForeignKey(Modele, models.DO_NOTHING, db_column='id_modele')
    url = models.ForeignKey(Image, models.DO_NOTHING, db_column='url')

    class Meta:
        managed = True
        db_table = 'prediction'
