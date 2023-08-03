from django import forms
from django.forms import ModelForm
from django.contrib import admin
from .models import Item,Item_images



class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class Item_imagesForm(forms.Form):
    images = MultipleFileField()
    class Meta:
        model=Item_images
        fields={'images',}

################# multiple files uploading verision that not working properly
# class Item_imagesForm(ModelForm):
#     images=forms.ImageField(widget=forms.FileInput(attrs={"class":"form-control", "multiple":True}))
#     class Meta:
#         model=Item_images
#         fields={'images',}
#################
class ItemForm(ModelForm):
    class Meta:
        model=Item
        fields={'title','thumbnail','description','price'}
        labels={
            'title':'name of the item',
            'thumbnail':'thumbnail',
            'description':'description',
            'price':'price',
        }
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'thumbnail':forms.FileInput(attrs={'class':'form-control'}),
            # 'description':forms.TextInput(attrs={'class':'form-control',}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
        }
