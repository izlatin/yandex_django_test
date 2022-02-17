from django.db import models


# Create your models here.
class Ivan(models.Model):
    name = models.TextField
    surname = models.TextField
    fathers_name = models.TextField
