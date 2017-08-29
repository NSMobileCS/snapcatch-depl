from __future__ import unicode_literals

from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=40, blank=True)
    fbook_auth_id = models.CharField(max_length=512, unique=True)
    def __str__(self):
        return "User {} (pk# = {})".format(self.name, self.pk)
    
class Animal(models.Model):
    name = models.CharField(max_length=40) 
    def __str__(self):
        return "Animal: {}".format(self.name)

class Catch(models.Model):
    user = models.ForeignKey(User, related_name='my_animal_pics')
    species = models.ForeignKey(Animal, related_name='pics_of')
    coordinates = models.CharField(max_length = 40, null=True, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(max_length = 400, blank=True)
    pic = models.ImageField(upload_to='userimages')
    def __str__(self):
        return "Catch Obj: {} caught by user {}".format