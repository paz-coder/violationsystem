from django.shortcuts import render
from django.http import HttpResponse

def MainPage(request):
	# if request.method == 'POST':
	# 	return HttpResponse (request.POST['attribute'])
	list_ = List.objects.get(id=list_id)
	return render(request, 'mainpage.html', {'npet': request.POST.get('attribute'),})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(npet=request.POST['pet'],nname =request.POST['owner'],nAddress=request.POST['address'],nBreed =request.POST['breed'],nDay =request.POST['birthday'], list=list_)
    return redirect(f'/msystem/{list_.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(npet=request.POST['pet'],nBreed =request.POST['breed'],nDay =request.POST['birthday'],list=list_)
    return redirect(f'/msystem/{list_.id}/')




