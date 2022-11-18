from django.db import models


# Create your models here.
class Poke(models.Model):
    id_pokemon = models.IntegerField()
    url_pokemon = models.CharField(max_length=255)
