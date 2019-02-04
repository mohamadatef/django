from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
class Data(models.Model):
    mrn = models.IntegerField('MRN')
    disc = models.CharField('Disc' , max_length = 200, default='None')
    text = models.TextField('text')
    tags = TaggableManager()
    

    def __str__(self):
        return self.disc