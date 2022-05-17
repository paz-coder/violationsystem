from django.shortcuts import render, redirect
from django.http import HttpResponse
from Svsystem.models import Stundentinfo

def MainPage(request):
    if request.method == 'POST':
        Stundentinfo.objects.create(Sname=request.POST['studentName'], 
            Sid= request.POST['ID'],
            Ssection= request.POST['Section'],
            Sviolation= request.POST['Violation'],)
        return redirect('/')
    reglist = Stundentinfo.objects.all()
    return render(request, 'mainpage.html',{'registered':reglist})