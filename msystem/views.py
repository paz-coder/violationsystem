from django.shortcuts import render
from django.http import  HttpResponse

def MainPage(request):
	return HttpResponse('<html><title>4ps Monitoring System</title></html>')
# Create your views here.
