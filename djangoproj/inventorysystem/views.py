from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h2>Supply Inventory System<h2> <h3>lets get it !!!!!<h3>')
