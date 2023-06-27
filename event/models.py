from django.contrib.auth.models import User
from django.db import models
from members.models import Profile
# Create your models here.

class Venue(models.Model):
    VENUE_TYPE=(
        ('indoor','indoor'),
        ('outdoor','outdoor'),
    )

    name=models.CharField('Venue Name',max_length=100,null=True)
    address=models.CharField('Venue Address',max_length=120)
    venue_type=models.CharField(max_length=30,choices=VENUE_TYPE,null=True,blank=True)
    note=models.TextField('Venue Note',max_length=500,blank=True)

    def __str__(self):
        return str(self.name)



class Event(models.Model):

    DURATION_TYPE=(
        ('1','1'),
        ('1.5','1.5'),
        ('2','2'),
        ('2.5','2.5'),
        ('3','3'),
        ('3.5','3.5'),
        ('4','4'),
        ('others','others'),
    )


    name=models.CharField('Event Name',max_length=100)
    event_datetime=models.DateTimeField('Event Date')
    duration=models.CharField(max_length=10,choices=DURATION_TYPE,null=True)
    organiser= models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    venue=models.ForeignKey(Venue,null=True,on_delete=models.SET_NULL)
    max_players=models.SmallIntegerField(null=True,blank=True)
    price=models.CharField('Event price',max_length=50,null=True,blank=True)
    activity_note=models.TextField(max_length=200, null=True,blank=True)
    payment_qr=models.ImageField(blank=True,null=True,upload_to='images/') # looking into detial for sizegetattr(): attribute name must be string
    RSVP=models.ManyToManyField(Profile,blank=True,null=True,through='RSVP_Profile_inter')
    # RSVP=models.ManyToManyField(Profile,blank=True,null=True)


    def __str__(self):
        return self.name

class RSVP_Profile_inter(models.Model):
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,on_delete=models.CASCADE)
    RSVP_datetime=models.DateTimeField(null=True,blank=True)
    note=models.CharField('note',max_length=50,null=True,blank=True)

    def __str__(self):
        return '%s %s' %(self.profile.first_name,self.profile.last_name)
