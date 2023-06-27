from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileForm
import datetime as dt

# Create your views here.
def user_register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'register successful')
            return redirect('update_profile',user.profile.id)
    else:
        form=UserRegisterForm
    return render(request,'authentication/user_register.html',{'form':form})

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request, ('login successful'))
            return redirect('all_events')
        else:
            messages.success(request, ('error happen when login, try again or contact admin'))
            return redirect('user_login')

    else:
        # messages.success(request, ('before if'))
        return render(request,'authentication/user_login.html',{})

def user_logout(request):
    logout(request)
    messages.success(request,'logout successful')
    return redirect('home')

def user_profile(request,profile_id):
    profile=Profile.objects.get(pk=profile_id)

    attended_events=profile.event_set.all().filter(event_datetime__range=[dt.datetime.now()-dt.timedelta(days=180),dt.datetime.now()])
    attending_events=profile.event_set.all().filter(event_datetime__range=[dt.datetime.now(),dt.timedelta(days=90)+dt.datetime.now()])
    print(attended_events.values())
    print(attending_events.values())
    return render(request,'authentication/profile.html',{'profile':profile,
                                                         'attended_events':attended_events,
                                                         'attending_events':attending_events})

def update_profile(request,profile_id):
    profile=Profile.objects.get(pk=profile_id)
    form=ProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        messages.success(request,'form valid and saved')
        form.save()
        return redirect('user_profile',profile_id)
    else:
        messages.success(request,'form invalid')
    return render(request,'authentication/update_profile.html',{'form':form})


def test(request):
    Profiles=Profile.objects.all()
    return render(request,'authentication/test.html',{'Profiles':Profiles})