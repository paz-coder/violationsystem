from django.db import models


class List(models.Model):
    pass


class Item(models.Model):
    npet = models.TextField(default='')
    nname = models.TextField(default='')
    nAddress = models.TextField(default='')
    nBreed = models.TextField(default='')
    nDay = models.TextField(default='') 
    list = models.ForeignKey(List, default=None, on_delete=models.PROTECT)

