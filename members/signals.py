from django.db.models.signals import post_save,pre_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender,instance,created,**kwargs):
    print('user got signal ')
    if created:
        print('new user registered')
        Profile.objects.create(user=instance)
        # Profile.objects.create(user=instance,first_name='fn',last_name='ln',age=5,email='test@test.com')


@receiver(post_save, sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()