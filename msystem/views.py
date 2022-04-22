
from django.shortcuts import render
from django.http import HttpResponse

def MainPage(request):
	return render(request, 'mainpage.html', {'Name': request.POST.get('NAME'), 'address': request.POST.get('ADDRESS'), 'age': request.POST.get('AGE'), 'dswd': request.POST.get('DSWD')})
