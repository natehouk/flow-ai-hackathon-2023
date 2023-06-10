from django.urls import path
from .views import *

urlpatterns = [
    path('latest-data/', get_data, name='latest-data'),
    path('latest-summary/', get_summary, name='latest-summary'),
    path('index/', index, name='index'),
]
