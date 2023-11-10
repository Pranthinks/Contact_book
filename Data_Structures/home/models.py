from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=12)
    relation = models.CharField(max_length=30)
    

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

# Create your models here.
