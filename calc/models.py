from django.db import models


class Operation(models.Model):
    a = models.FloatField()
    operators = models.CharField(max_length=3)
    b = models.FloatField()
    result = models.FloatField()
    user = models.ForeignKey()
