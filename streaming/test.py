import time
from .models import Data
def tt():
    return time.now()

def call():
    i = 0
    while True:
        print(i,"calling")
        i+=1
        time.sleep(1)
        Data.objects.create(value=f'test-{i}')
