# Generated by Django 3.2.12 on 2024-05-02 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0003_alter_enregistrement_cours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enregistrement',
            name='cours',
            field=models.FileField(default='', upload_to='media'),
        ),
    ]
