# Generated by Django 5.1 on 2024-09-02 19:02

from django.db import migrations, models

import core.services.file_services


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_alter_carmodel_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carphotomodel',
            options={'ordering': ('id',)},
        ),
        migrations.AlterField(
            model_name='carphotomodel',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=core.services.file_services.FileService.upload_car_photo),
        ),
        migrations.AlterModelTable(
            name='carphotomodel',
            table='car_photos',
        ),
    ]
