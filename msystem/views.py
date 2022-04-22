
from django.shortcuts import render
from django.http import HttpResponse

def MainPage(request):
	# if request.method == 'POST':
	# 	return HttpResponse (request.POST['newname'])
	return render(request, 'mainpage.html', {'NewName': request.POST.get('newname'),})
def New_list(request):

	return render(request, 'mainpage.html', {'Newaddress': request.POST.get('add'),})

