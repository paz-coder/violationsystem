from django.db import models

    
class List(models.Model):
    pass

class Item(models.Model):    
    Name = models.TextField(default='')
    Address = models.TextField(default='')  
    Age = models.TextField(default='')
    Dswd = models.TextField(default='')




    list = models.ForeignKey(List, default=None, on_delete=models.PROTECT)