from django.db import models
import time

class Data(models.Model):
    value = models.CharField(max_length=255)
    update = models.BooleanField(default=False)
    lastPart = models.BooleanField(default=False)

class Summaries(models.Model):
    value = models.CharField(max_length=255)
    update = models.BooleanField(default=False)


class DataAPIs(models.Model):
    source = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    update = models.BooleanField(default=False)
    lastPart = models.BooleanField(default=False)

class SummariesAPIs(models.Model):
    value = models.CharField(max_length=255)
    update = models.BooleanField(default=False)


class Prompts(models.Model):
    value = models.CharField(max_length=255)
    update = models.BooleanField(default=False)


last_object = Prompts.objects.last()
if last_object is None:
    Prompts.objects.create(value=f"",update=False)