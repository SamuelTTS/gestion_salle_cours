# Generated by Django 5.0.1 on 2024-01-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_salle', '0007_reservation_terminee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='matiere',
            field=models.CharField(max_length=100),
        ),
    ]
