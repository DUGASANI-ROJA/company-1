
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Company(models.Model):
    GENDER_CHOICE = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    DESIGNATION_CHOICE = (
        ('CEO', 'Ceo'),
        ('CTO', 'Cto'),
        ('CFO', 'Cfo'),
        ('SR AS', 'Sr as'),
        ('SR TS', 'Sr ts'),
        ('TL', 'Tl'),
        ('JR STAFF', 'Jr staff')
    )

    name = models.CharField(max_length=100)
    age = models.IntegerField(default=2)
    phno = models.IntegerField(default=10)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    email = models.EmailField()
    profile_pic = models.ImageField(upload_to='upload/')
    designation = models.CharField(max_length=100, choices=DESIGNATION_CHOICE)

    def __str__(self):
        return self.name


