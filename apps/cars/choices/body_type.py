from django.db import models


class BodyTypeChoices(models.TextChoices):
    HatchBack = 'HatchBack',
    Sedan = 'Sedan',
    Coupe = 'Coupe',
    Wagon = 'Wagon',
    Jeep = 'Jeep',
    Roadster = 'Roadster',
    Convertible = 'Convertible',
    Sport_Car = 'Sport Car',
    Crossover = 'Crossover',
    Pickup = 'Pickup',
    Minivan = 'Minivan',
    Van = 'Van',
    Limousine = 'Limousine',



