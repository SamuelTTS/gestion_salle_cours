# Generated by Django 5.0.1 on 2024-01-20 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_salle', '0002_reservation_matiere_salle_capacite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='matiere',
            field=models.CharField(default='', max_length=100),
        ),
    ]
