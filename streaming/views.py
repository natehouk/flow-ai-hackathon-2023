from django.core import serializers
from django.http import JsonResponse
from django.views import View
from .models import Data
from django.shortcuts import render

def get(request):
    latest_data = Data.objects.last()
    if latest_data is None:
    	return JsonResponse({'latest_data': False})
    # call()
    value = latest_data.value
    update = latest_data.update
    # print(f"INFO {value} {update}")
    if not latest_data.update:
	    latest_data_to_update = Data.objects.last()
	    latest_data_to_update.update = True
	    latest_data_to_update.save()
    if not update:
        return JsonResponse({'latest_data': latest_data.value})
    else:
    	return JsonResponse({'latest_data': False})
    	

def temp(request):

	return render(request, 'stream.html')

