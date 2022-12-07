from django.db import models


class Markers(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    latlan = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=255)
    effect = models.CharField(max_length=255)
    bike = models.CharField(max_length=255)
    car = models.CharField(max_length=255)
