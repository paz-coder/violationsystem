# from django.shortcuts import render
# from django.http import HttpResponse

# def MainPage(request):
# 	return render (request, 'mainpage.html')

from django.shortcuts import render
from django.http import HttpResponse

def MainPage(request):
	# if request.method == 'POST':
	# 	return HttpResponse (request.POST['attribute'])
	return render(request, 'mainpage.html', {'NewName': request.POST.get('attribute'),})
def New_list(request):
	# if request.method == 'POST':
	# 	return HttpResponse (request.POST['attribute'])
	return render(request, 'mainpage.html', {'Newaddress': request.POST.get('add'),})

