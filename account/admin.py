from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import abonnement


class AbonnementInline(admin.StackedInline):
    model = abonnement


class CustomUserAdmin(UserAdmin):
    inlines = (AbonnementInline,)


# Désenregistrez le modèle User par défaut
admin.site.unregister(User)

# Enregistrez à nouveau le modèle User avec votre admin personnalisé
admin.site.register(User, CustomUserAdmin)