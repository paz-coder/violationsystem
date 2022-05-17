from django.db import models

class Stundentinfo(models.Model):
    Sname = models.TextField(default='')
    Sid = models.TextField(default='')
    Ssection = models.TextField(default='')
    Sviolation = models.TextField(default='')

