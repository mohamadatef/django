from django.db import models

# Create your models here.
class Data(models.Model):
    mrn = models.IntegerField('MRN')
    disc = models.CharField('Disc' , max_length = 200, default='None')
    text = models.TextField('text')

    def __str__(self):
        return self.disc