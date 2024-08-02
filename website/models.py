from django.db import models

# Create your models here.
class Services(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=500,default='')
    icon = models.CharField(max_length=100,default='')
    
    def __str__(self):
        return self.name