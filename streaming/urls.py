from django.urls import path
from .views import *

urlpatterns = [
    path('latest-data/', get_data, name='latest-data'),
    path('latest-summary/', get_summary, name='latest-summary'),
    path('post-prompt/', post_prompt, name='post-prompt'),
    path('', index, name='index'),
]
