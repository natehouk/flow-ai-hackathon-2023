from django.db import models
import time

class Data(models.Model):
    value = models.CharField(max_length=255)
    update = models.BooleanField(default=False)


class Summaries(models.Model):
    value = models.CharField(max_length=255)
    update = models.BooleanField(default=False)
