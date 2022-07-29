from django.shortcuts import render


def home(request):
    return render(request, 'task/home.html')

def login(request):
    return render(request, 'task/login.html')

def esupplydelivery(request):
    return render(request, 'task/esupplydelivery.html')

def nsupplydelivery(request):
    return render(request, 'task/nsupplydelivery.html')

def supplyrequest(request):
    return render(request, 'task/supplyrequest.html')

def supplywithdraw(request):
    return render(request, 'task/supplywithdraw.html')

def statuslimit(request):
    return render(request, 'task/statuslimit.html')

def eequipdelivery(request):
    return render(request, 'task/eequipdelivery.html')

def nequipdelivery(request):
    return render(request, 'task/nequipdelivery.html')

def equiprequest(request):
    return render(request, 'task/equiprequest.html')

def equipwithdraw(request):
    return render(request, 'task/equipwithdraw.html')

def equipreturn(request):
    return render(request, 'task/equipreturn.html')

def storagemapping(request):
    return render(request, 'task/storagemapping.html')