from django.shortcuts import render,redirect
from .models import Blog

from django.conf import settings


# Create your views here.
def all_blogs(request):
    blogs=Blog.objects.all().order_by('-datetime')
    return render(request,'blog/all_blogs.html',{'blogs':blogs})


def blog_detail(request,blog_id):
    blog=Blog.objects.get(pk=blog_id)

    return render(request, 'blog/blog_detail.html', {'blog': blog})

def add_blog(request):
    pass
