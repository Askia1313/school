from django.contrib import admin
from django.urls import path, include
from .views import affiche, cours, telecharger_cours, acceuil, paiement

app_name = 'APP1'

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('cours/', cours, name='cours'),
    path('affiche/', affiche, name='affiche'),
    path('telecharger-cours/<int:enregistrement_id>/', telecharger_cours, name='telecharger_cours'),
    path('', acceuil, name='acceuil'),
    path('paiement/', paiement, name='paiement'),
]

