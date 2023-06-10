from django.urls import path
from .views import get, temp

urlpatterns = [
    path('latest-data/', get, name='latest-data'),
    path('index/', temp, name='index'),
]
