from django.shortcuts import redirect, render
from django.http import HttpResponse    
from msystem.models import Member


#def MainPage(request):
	#return render(request, 'mainpage.html', {'Name': request.POST.get('Name'), 'Address': request.POST.get('address'), 'Age': request.POST.get('age'), 'Dswd': request.POST.get('dswd')})


def MainPage(request): 
 
 if request.method == 'POST':
        Member.objects.create(Name=request.POST['Name'], 
            Address= request.POST['address'],
            Age= request.POST['age'],
            Dswd= request.POST['dswd'],)
        return redirect('/')
        reglist = Member.objects.all()
        return render(request, 'mainpage.html',{'items':reglist})

  
'''

def view_list(request, list_id):    
   list_ = List.objects.get(id=list_id)
   return render(request, 'mainpage.html', {'list': list_})
   
def new_list(request):    
   list_ = List.objects.create()
   Member.objects.create(Name=request.POST['Name'], Address=request.POST['address'], Age=request.POST['age'], Dswd=request.POST['dswd'],list=list_)
   return redirect(f'/msystem/{list_.id}/')'''

'''  
def add_item(request, list_id):    
   list_ = List.objects.get(id=list_id)    
   Item.objects.create(Name=request.POST['Name'], Address=request.POST['address'], Age=request.POST['age'], Dswd=request.POST['dswd'],list=list_)
   return redirect(f'/msystem/{list_.id}/') '''



'''def MainPage(request): 
   return render(request, 'mainpage.html') 	
  


def view_list(request, list_id):    
   list_ = List.objects.get(id=list_id)
   return render(request, 'my2.html', {'list': list_})
   
def new_list(request):    
   list_ = List.objects.create()
   Item.objects.create(text=request.POST['itext'], list=list_)
   return redirect(f'/MNList/{list_.id}/')
  
   #return redirect('/MNList/the-only-list-in-the-world/')
   #Item.objects.create(text=request.POST['itext'])
   #return redirect('/MNList/the-only-list-in-the-world/')
   #return redirect('/MNList/the-only-list-in-the-world/')
   
   
def add_item(request, list_id):    
   list_ = List.objects.get(id=list_id)    
   Item.objects.create(text=request.POST['itext'], list=list_)
   return redirect(f'/MNList/{list_.id}/')'''