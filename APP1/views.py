from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from APP1.models import enregistrement

from datetime import datetime
from random import randint
def affiche(request):
    return render(request, 'affiche.html')

def acceuil(request):
    return render(request, 'acceuil.html')

def cours(request):
    posts = enregistrement.objects.all()
    matieres = enregistrement.objects.values_list('matiere', flat=True).distinct()
    return render(request, 'cours.html', {'posts': posts, 'matieres': matieres})

def telecharger_cours(request, enregistrement_id):
    enregistrement_obj = get_object_or_404(enregistrement, pk=enregistrement_id)
    fichier_cours = enregistrement_obj.cours.path
    with open(fichier_cours, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename={enregistrement_obj.titre}.pdf'
        return response


# Dans votre fichier views.py


import requests
import json


# def paiement(request):
#     if request.method == 'POST':
#         # Récupérer les données du formulaire
#         nom = request.POST.get('nom')
#         prenom = request.POST.get('prenom')
#         email = request.POST.get('email')
#         ID= f"AK{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{randint(1, 10000)}"
#
#         # Envoi de la requête de paiement à l'API Ligdicash
#         url = "https://app.ligdicash.com/pay/v01/redirect/checkout-invoice/create"
#         api_key = "REV9DJR33TZ6J4I4O"
#         bearer_token = ""
#
#         headers = {
#             "Apikey": api_key,
#             "Authorization": f"Bearer {bearer_token}",
#             "Accept": "application/json",
#             "Content-Type": "application/json",
#             "Cookie": "ligdicash=2vcanu1d0om08g4m3a6jn0c1im"
#         }
#
#         payload = {
#             "commande": {
#                 "invoice": {
#                     "items": [
#                         {
#                             "name": "abonnement",
#                             "description": "abonnement pour suivre des cours en ligne sur educa",
#                             "quantity": 1,
#                             "unit_price": 100,
#                             "total_price": 100
#                         }
#                     ],
#                     "total_amount": 100,
#                     "devise": "XOF",
#                     "description": "abonnement a educa",
#                     "customer": "",
#                     "customer_firstname": nom,
#                     "customer_lastname": prenom,
#                     "customer_email": email,
#                     "external_id": "",
#                     "otp": ""
#                 },
#                 "store": {
#                     "name": "EDUCA",
#                     "website_url": "http://127.0.0.1:8000/APP1/"
#                 },
#                 "actions": {
#                     "cancel_url": "http://127.0.0.1:8000/APP1/paiement/",
#                     "return_url": "http://127.0.0.1:8000/APP1/paiement/",
#                     "callback_url": "http://localhost"
#                 },
#                 "custom_data": {
#                     "transaction_id": ID,
#
#                 }
#             }
#         }
#
#         response = requests.post(url, headers=headers, data=json.dumps(payload))
#
#         # Traitez la réponse ici, par exemple :
#         if response.status_code == 00:
#             response_data = response.json()
#             # Faites quelque chose avec les données de réponse, par exemple enregistrez-les dans votre modèle de données
#
#             return render(request, 'cours.html', {'response_data': response_data})
#         else:
#             # Gérez les cas où la requête a échoué
#             return HttpResponse("Une erreur s'est produite lors du traitement de la demande de paiement.")
#     else:
#         # Afficher le formulaire HTML
#         return render(request, 'cours.html')

import requests
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from random import randint

def payin_with_redirection(transaction_id, nom, prenom, email):
    url = "https://app.ligdicash.com/pay/v01/redirect/checkout-invoice/create"
    payload = {
        "commande": {
            "invoice": {
                "items": [
                    {
                        "name": "Nom de l'article ou du service ou du produit",
                        "description": "Description du service ou du produit",
                        "quantity": 1,
                        "unit_price": 100,
                        "total_price": 100
                    }
                ],
                "total_amount":100,
                "devise": "XOF",
                "description": "Description de la commande des produits ou des services",
                "customer": "",
                "customer_firstname": nom,
                "customer_lastname": prenom,
                "customer_email": email
            },
            "store": {
                "name": "EDUCA",
                "website_url": "http://localhost/APP1/"
            },
            "actions": {
                "cancel_url": "http://127.0.0.1:8000/APP1/",
                "return_url": "http://localhost/APP1/cours",
                "callback_url": "http://localhost/APP1/cours"
            },
            "custom_data": {
                "transaction_id": transaction_id
            }
        }
    }
    headers = {
        "Apikey": "MAGPMLT3QFJLIPUDN",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZF9hcHAiOjE1MDA5LCJpZF9hYm9ubmUiOjg5OTQyLCJkYXRlY3JlYXRpb25fYXBwIjoiMjAyNC0wNC0wOCAwODozMjoyNCJ9.NRcyHfFO8OyaXOaklZ2DJ2Arf-gV8OXGfMIELQzdw88",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def paiement(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        transaction_id = f"AK{datetime.now().strftime('%Y%m%d_%H%M')}.C{randint(5, 100000)}"


        # Appel à l'API Ligdicash pour créer une commande
        redirect_payin = payin_with_redirection(transaction_id, nom, prenom, email)

        # Vérifiez et traitez la réponse
        if 'response_code' in redirect_payin:
            response_code = redirect_payin['response_code']
            if response_code == "00":
                # Redirection vers l'URL de paiement
                return redirect(redirect_payin['response_text'])
            else:
                # Gestion des erreurs
                response_text = redirect_payin.get('response_text', '')
                description = redirect_payin.get('description', '')
                return HttpResponse(f"Erreur {response_code}: {response_text}<br><br>{description}")
        else:
            return HttpResponse("Une erreur s'est produite lors de la demande de paiement.")
    else:
        # Afficher le formulaire HTML
        return render(request, 'cours.html')

