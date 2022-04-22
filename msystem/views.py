
from django.shortcuts import render
from django.http import HttpResponse

def MainPage(request):
	return render(request, 'mainpage.html', {'Name': request.POST.get('Name'), 'Address': request.POST.get('address'), 'Age': request.POST.get('age'), 'Dswd': request.POST.get('dswd'), 'Member': request.POST.get('member')})
