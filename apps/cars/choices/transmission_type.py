from django.db import models


class TransmissionType(models.TextChoices):
    mechanics = "mechanics",
    automatic = "automatic",
    tiptronic = "tiptronic",
    robot = "robot",
    variator = "variator",
    dct = "DCT"
