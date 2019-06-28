from django.db import models


class Rooms(models.Model):
    name = models.CharField(max_length=127, primary_key=True)
    password = models.CharField(max_length=31)
