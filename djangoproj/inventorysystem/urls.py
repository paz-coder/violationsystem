from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='inventorysystem_home'),
    path('login/', views.login, name='inventorysystem_login'),
    path('esupplydelivery/', views.esupplydelivery, name='inventorysystem_esupplydelivery'),
    path('nsupplydelivery/', views.nsupplydelivery, name='inventorysystem_nsupplydelivery'),
    path('supplyrequest/', views.supplyrequest, name='inventorysystem_supplyrequest'),
    path('supplywithdraw/', views.supplywithdraw, name='inventorysystem_supplywithdraw'),
    path('statuslimit/', views.statuslimit, name='inventorysystem_statuslimit'),
    path('eequipedelivery/', views.eequipdelivery, name='inventorysystem_eequipdelivery'),
    path('nequipedelivery/', views.nequipdelivery, name='inventorysystem_nequipdelivery'),
    path('equiprequest/', views.equiprequest, name='inventorysystem_equiprequest'),
    path('equipwithdraw/', views.equipwithdraw, name='inventorysystem_equipwithdraw'), 
    path('equipreturn/', views.equipreturn, name='inventorysystem_equipreturn'), 
    path('storagemapping/', views.storagemapping, name='inventorysystem_storagemapping'),      
]
