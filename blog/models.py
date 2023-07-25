from django.db import models

# Create your models here.
from django.db import models
from members.models import Profile,User
from ckeditor.fields import RichTextField


class Blog(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile,null=True,on_delete=models.SET_NULL)
    title=models.CharField('Title',max_length=200,null=True)
    body=RichTextField(null=True)
    photo=models.ImageField(blank=True,null=True,upload_to='blog/')
    snippet=models.TextField('snippet',max_length=300,null=True)
