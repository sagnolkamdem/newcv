# Generated by Django 3.0.3 on 2021-03-08 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mon_CV', '0009_auto_20210308_0818'),
    ]

    operations = [
        migrations.AddField(
            model_name='competence',
            name='type_de_la_competence',
            field=models.CharField(blank=True, choices=[('L', 'LANGUAGE'), ('F', 'FRAMEWORK'), ('GP', 'GESTION DE PROJET'), ('L', 'LANGUAGE DE PROGRAMMATION'), ('BD', 'BASE DE DONNEES')], max_length=200),
        ),
    ]