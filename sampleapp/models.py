from django.db import models
class Uer(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)