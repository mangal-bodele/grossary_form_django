from django.db import models

class Grossary(models.Model):
    store = models.CharField(max_length=10)
    item = models.CharField(max_length=10)
    quanitity = models.IntegerField()
    price = models.IntegerField()
    pay_mode = models.CharField(max_length=10)
    
