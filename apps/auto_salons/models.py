from django.db import models

from core.models import BaseModel


class AutoSalonModel(BaseModel):
    class Meta:
        db_table = 'auto_salons'
        ordering = ['id']

    name = models.CharField(max_length=25)