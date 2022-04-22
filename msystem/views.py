
from django.shortcuts import render
from django.http import HttpResponse

def MainPage(request):
	return render(request, 'mainpage.html', {'Name': request.POST.get('Name'), 'address': request.POST.get('Address1'), 'age': request.POST.get('Age1'), 'dswd': request.POST.get('Dswd1')})
