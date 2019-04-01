from django.db import models
from django.db.models import CharField, ForeignKey, ImageField
from django.conf import settings
from django.utils import timezone




class Nija(models.Model):
    SEX = (
        ('F', 'Female'),
        ('M', 'Male'),
    )

    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    gender = CharField(max_length=1, choices=SEX)
   

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

