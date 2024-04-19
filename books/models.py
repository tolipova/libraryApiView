from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200 )
    subtitle = models.CharField(max_length=200 )
    author = models.CharField(max_length=100)
    isbn = models.IntegerField()
    price = models.DecimalField(max_digits=30 , decimal_places=2)
    
    
    