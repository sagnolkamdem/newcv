# Generated by Django 3.0.3 on 2021-03-08 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mon_CV', '0014_auto_20210308_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competence',
            name='statut_competence',
            field=models.CharField(blank=True, choices=[('Advanced', 'Advance'), ('Intermediate', 'Intermediate'), ('Beginner', 'Beginner')], max_length=200),
        ),
    ]
