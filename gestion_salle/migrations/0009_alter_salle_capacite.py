# Generated by Django 5.0.1 on 2024-01-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_salle', '0008_alter_reservation_matiere'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salle',
            name='capacite',
            field=models.IntegerField(default=0),
        ),
    ]
