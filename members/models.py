from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import datetime
class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    # name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)


class Profile(models.Model):
    PLAYER_TYPE=(
        ('xiuxian','休闲'),
        ('yeren','野人'),
    )

    YEAR_CHOICES = [(r, r) for r in range(2010, datetime.date.today().year + 1)]

    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    first_name=models.CharField('First Name',max_length=50,null=True,)
    last_name=models.CharField('Last Name',max_length=50,null=True,)
    nick_name=models.CharField('Nick Name',max_length=50,blank=True,null=True)
    # age = models.IntegerField('Member Age',blank=True,null=True)
    # email=models.EmailField('Member Email',max_length=50,null=True,)
    phone=models.CharField('Member Phone',max_length=50,blank=True,null=True)
    shirt_size= models.CharField('Shirt Size',max_length=20,null=True,blank=True)
    retire_year=models.IntegerField(choices=YEAR_CHOICES,null=True,blank=True)
    bio=models.TextField('Member Bio', max_length=500,null=True,blank=True)


    # player_type=models.CharField(max_length=20,choices=PLAYER_TYPE,null=True,blank=True)


    # def __str__(self):
    #     return '%s %s (%s)' %( self.first_name,self.last_name,self.nick_name)

