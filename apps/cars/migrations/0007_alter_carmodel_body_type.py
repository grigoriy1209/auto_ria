# Generated by Django 5.1 on 2024-08-30 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_carmodel_auto_salon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='body_type',
            field=models.CharField(choices=[('HatchBack', 'Hatchback'), ('Sedan', 'Sedan'), ('Coupe', 'Coupe'), ('Wagon', 'Wagon'), ('Jeep', 'Jeep'), ('Roadster', 'Roadster'), ('Convertible', 'Convertible'), ('Sport Car', 'Sport Car'), ('Crossover', 'Crossover'), ('Pickup', 'Pickup'), ('Minivan', 'Minivan'), ('Van', 'Van'), ('Limousine', 'Limousine')], max_length=20),
        ),
    ]
