# Generated by Django 3.2.12 on 2024-05-24 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonnement',
            name='payer',
            field=models.BooleanField(default=False),
        ),
    ]
