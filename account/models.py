from django.contrib.auth.models import User
from django.db import models

class abonnement(models.Model):
    compte = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=50, default='0')
    payer = models.BooleanField(default=False)

    def __str__(self):
        return self.code
