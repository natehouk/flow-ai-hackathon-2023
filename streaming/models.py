from django.db import models
import time

class Data(models.Model):
    value = models.CharField(max_length=255)

i = 0
def call():
    global i
    
    while True:
        print(i,"calling")
        i+=1
        time.sleep(1)
        Data.objects.create(value=f'test-{i}')
        return 
