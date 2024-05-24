from django.contrib import admin

# Register your models here.
from APP1.models import enregistrement


@admin.register(enregistrement)

class enregistrementAdmin(admin.ModelAdmin):
    list_display = ('titre', 'prof', 'matiere', 'date')




