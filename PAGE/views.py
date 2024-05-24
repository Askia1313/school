from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
def mes_cours(request):
    return render(request, 'mes_cours.html')