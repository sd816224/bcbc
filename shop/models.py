from django.db import models
from ckeditor.fields import RichTextField
import datetime

class Item(models.Model):
    title = models.TextField('Title', max_length=300, null=True)
    thumbnail = models.ImageField(blank=True, null=True, upload_to='shop/thumbnail/')
    description = RichTextField(null=True)
    price=models.IntegerField()
    slug=models.SlugField(default='',null=False)

    def __str__(self):
        return self.title

class Item_images(models.Model):
    item=models.ForeignKey(Item,blank=True,null=True,on_delete=models.CASCADE)
    # images=models.ImageField(blank=True,null=True,upload_to=f'shop/{int(datetime.datetime.now().timestamp())}/')
    images=models.ImageField(blank=True,null=True,upload_to=f'shop/')

    def __str__(self):
        return self.item.title

