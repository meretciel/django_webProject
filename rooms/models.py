from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    SEX_CHOICES = (
        ('girl', 'girl only'),
        ('boy', 'boy only'),
        ('mixed', 'boy/girl'),
    )

    ROOMTYPE_CHOICES = (
        ('living', 'living room'),
        ('bedroom_1', 'master bedroom'),
        ('bedroom_2',  'bedroom'),
        ('bedroom_3',  'small bedroom'),
    )


    # room information
    room_type = models.CharField(max_length=30, choices=ROOMTYPE_CHOICES)
    building_name = models.CharField(max_length=40)
    location      = models.CharField(max_length=40)

    # dates inforation includes the start date of the rent
    # and the duration for the rent
    start_date = models.DateField()
    end_date   = models.DateField()
    lease_term = models.IntegerField(default=-1) # unit is month


    # money related fields
    rent = models.FloatField()
    security_deposit = models.FloatField(default=0)


    # other
    is_available = models.BooleanField(defaut=True)
    sex = models.CharField(max_length=10,choices=SEX_CHOICES, default='mixed')
    link = models.URLField()
    description = models.TextField()

