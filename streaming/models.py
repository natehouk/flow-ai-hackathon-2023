from django.db import models
import time

class Data(models.Model):
    value = models.CharField(max_length=255)
    update = models.BooleanField(default=False)
    lastPart = models.BooleanField(default=False)

class Summaries(models.Model):
    value = models.CharField(max_length=255)
    update = models.BooleanField(default=False)

class Prompts(models.Model):
    value = models.CharField(max_length=255)
    update = models.BooleanField(default=False)


last_object = Prompts.objects.last()
if last_object is None:
    Prompts.objects.create(value=f"summarize the incoming data, I would like to know the opinions of main person speaking",update=False)