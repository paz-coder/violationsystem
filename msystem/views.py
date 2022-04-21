from django.shortcuts import render, redirect
from django.http import HttpResponse
from msystem.models import Item, List


def home_page(request):
    items = Item.objects.all()
    return render(request, 'homepage.html',{'items' : items})
    


def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    return render(request, 'mainpage.html', {'list': list_})


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(npet=request.POST['pet'],nname =request.POST['owner'],nAddress=request.POST['address'],nBreed =request.POST['breed'],nDay =request.POST['birthday'], list=list_)
    return redirect(f'/Msystem/{list_.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(npet=request.POST['pet'],nBreed =request.POST['breed'],nDay =request.POST['birthday'],list=list_)
    return redirect(f'/Msystem/{list_.id}/')
