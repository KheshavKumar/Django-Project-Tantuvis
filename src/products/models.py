from django.db import models



# Create your models here.
class Product(models.Model):
    #"""
    Title       = models.CharField(max_length=140)#max_length is required
    Description = models.TextField( blank= True, null=True)
    Price       = models.DecimalField(max_digits=100, decimal_places=2)
    Summary     = models.TextField()#null=True is wrt database and blank=True is wrt the form submitted
    featured    = models.BooleanField(default=True)
    #"""
    
    """
    Title       =  models.TextField(default='This is cool')
    Description =  models.TextField(default='This is cool')
    Price       =  models.TextField(default='This is cool')
    Summary     = models.TextField(default='This is cool')
    """