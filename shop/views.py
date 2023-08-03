from django.shortcuts import render,redirect
from django.utils.text import slugify

from .models import Item, Item_images
from .forms import Item_imagesForm,ItemForm
from django.contrib import messages

# Create your views here.
def all_items(request):
    print(request)
    all_items=Item.objects.all()
    # all_items=Item.objects.all().order_by('-datetime')
    return render(request,'shop/all_items.html',{'all_items':all_items})



def item_detail(request,slug):
    item=Item.objects.get(slug=slug)
    images=item.item_images_set.all()

    return render(request, 'shop/item_detail.html', {'item':item,'images':images})

def add_item(request):
    if request.method=='POST':
        files=request.FILES.getlist('images')
        item_form=ItemForm(request.POST,request.FILES)
        if item_form.is_valid():
            item=item_form.save(commit=False)
            item.slug=slugify(item.title+'-'+str(item.price))
            item.save()
            messages.success(request,'item created successfuly')
            for file in files:
                Item_images.objects.create(item=item,images=file)
            return redirect('all_items')
        else:
            messages.error(request,'something wrong happen in form')
    else:
        item_form=ItemForm
        images_form=Item_imagesForm
    return render(request,'shop/add_item.html',{'item_form':item_form,'images_form':images_form})

def cart(request):
    pass

def checkout(request):
    pass