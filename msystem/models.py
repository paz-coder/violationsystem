from django.db import models

    
class List(models.Model):
    pass

class Member(models.Model):    
    Name = models.TextField(default='')
    Address = models.TextField(default='')  
    Age = models.TextField(default='')
    Dswd = models.TextField(default='')

'''class Item(models.Model):    
     = models.TextField(default='')
     = models.TextField(default='')  
     = models.TextField(default='')
     = models.TextField(default='')

class Program(models.Model):    
     = models.TextField(default='')
     = models.TextField(default='')  
     = models.TextField(default='')
     = models.TextField(default='')

class Item(models.Model):    
     = models.TextField(default='')
     = models.TextField(default='')  
     = models.TextField(default='')
     = models.TextField(default='')

class Item(models.Model):    
     = models.TextField(default='')
     = models.TextField(default='')  
     = models.TextField(default='')
     = models.TextField(default='')'''







    list = models.ForeignKey(List, default=None, on_delete=models.PROTECT)