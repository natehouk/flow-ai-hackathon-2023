from django.urls import path
from .views import *

urlpatterns = [
    path('latest-data/', get_data, name='latest-data'),
    path('latest-summary/', get_summary, name='latest-summary'),
    path('latest-data-api/', get_data_apis, name='latest-data-api'),
    path('latest-summary-api/', get_summary_api, name='latest-summary-api'),
    path('post-prompt/', post_prompt, name='post-prompt'),
    path('', index, name='index'),
    path('add-source/', add_source, name='add-source'),
    path('kill-source/', kill_source, name='kill-source'),
]
