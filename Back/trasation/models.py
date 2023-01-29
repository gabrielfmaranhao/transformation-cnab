from django.db import models


class Trasation(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True, editable=False)
    type = models.IntegerField(null=False, unique=True)
    description = models.TextField(null=False, unique=True)
    nature = models.TextField(null=False)
    signal = models.TextField(null=False)


