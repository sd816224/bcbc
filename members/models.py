from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    first_name=models.CharField('First Name',max_length=50,null=True,)
    last_name=models.CharField('Last Name',max_length=50,null=True,)
    nick_name=models.CharField('Nick Name',max_length=50,blank=True,null=True)
    age = models.IntegerField('Member Age',blank=True,null=True)
    email=models.EmailField('Member Email',max_length=50,null=True,)
    phone=models.CharField('Member Phone',max_length=50,blank=True,null=True)
    shirt_size= models.CharField('Shirt Size',max_length=20,null=True,blank=True)
    bio=models.TextField('Member Bio', max_length=500,null=True,blank=True)

    caiji=1
    master=2
    PLAYER_TYPE=(
        (caiji,'caiji'),
        (master,'master'),
    )

    player_type=models.PositiveSmallIntegerField(choices=PLAYER_TYPE,null=True,blank=True)


    def __str__(self):
        return '%s %s (%s)' %( self.first_name,self.last_name,self.nick_name)
