from django.db import models
from datetime import date

# Create your models here.
class enregistrement(models.Model):
    prof = models.CharField(max_length=50, default='anonyme')
    matiere = models.CharField(max_length=50)
    titre = models.CharField(max_length=50)
    date = models.DateField(default=date.today)
    cours = models.FileField(upload_to="media", blank=False, null=False , default='')

    def __str__(self):
        return self.titre



