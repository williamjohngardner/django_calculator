from django.contrib.auth.models import User
from django.db import models


class Operation(models.Model):
    a = models.FloatField()
    operators = models.CharField(max_length=1)
    b = models.FloatField()
    result = models.FloatField()
    user = models.ForeignKey(User)
