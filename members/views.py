from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth import authenticate,login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
# from django.contrib.auth.models import User
from .models import Profile,User
from .forms import ProfileForm
from .decorators import user_not_authenticated
from .token import account_activation_token
from django.conf import settings

import datetime as dt
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

# import allauth.account.views

def activateEmail(request,user,to_email):
    subject='Activate your user account'
    message=render_to_string('authentication/acc_active_email.html',{
        'user':user.email,
        'domain':get_current_site(request).domain,
        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
        'token':account_activation_token.make_token(user),
        'protocol':'https' if request.is_secure() else 'http'
    })
    from_email=settings.EMAIL_HOST_USER
    if send_mail(subject=subject,message=message,from_email=from_email,recipient_list=[to_email])==1:
        messages.success(request,f'Please check Email inbox to activate link to confirm the registration')
    else:
        messages.error(request,f'problem sending email to {to_email}, check if you typing correctly')


def activate(request,uidb64,token):
    try:
        uid=force_str(urlsafe_base64_decode(uidb64))
        user=User.objects.get(pk=uid)
    except:
        user=None
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active=True
        user.save()
        user.backend='django.contrib.auth.backends.ModelBackend'
        login(request,user)
        messages.success(request,'thank you for email confirmation, now you are login your account, please update your profile to let everyone knows who you are. ')
        return redirect('user_profile') # go to profile to update
    else:
        messages.error(request,'activation link is invalid, please contact admin')
        return redirect('home')

# Create your views here.
@user_not_authenticated
def user_register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active=False
            user.save()
            email=form.cleaned_data.get('email')
            activateEmail(request,user,email)
            # # print(user)
            # email=form.cleaned_data['email']
            # password=form.cleaned_data['password1']
            # user=authenticate(username=email,password=password)
            # login(request,user)
            # messages.success(request,'register successful')
            # return redirect('update_profile',user.profile.id)
            return redirect('home')
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

def user_profile(request):
    profile=request.user.profile

    attended_events=profile.event_set.all().filter(event_datetime__range=[dt.datetime.now()-dt.timedelta(days=180),dt.datetime.now()])
    attending_events=profile.event_set.all().filter(event_datetime__range=[dt.datetime.now(),dt.timedelta(days=90)+dt.datetime.now()])
    # print(attended_events.values())
    # print(attending_events.values())
    return render(request,'authentication/profile.html',{'profile':profile,
                                                         'attended_events':attended_events,
                                                         'attending_events':attending_events})

def other_profile(request,profile_id):
    profile=Profile.objects.get(pk=profile_id)
    attended_events=profile.event_set.all().filter(event_datetime__range=[dt.datetime.now()-dt.timedelta(days=180),dt.datetime.now()])
    attending_events=profile.event_set.all().filter(event_datetime__range=[dt.datetime.now(),dt.timedelta(days=90)+dt.datetime.now()])

    return render(request, 'authentication/profile.html', {'profile': profile,
                                                           'attended_events': attended_events,
                                                           'attending_events': attending_events})
def update_profile(request,profile_id):
    profile=Profile.objects.get(pk=profile_id)
    form=ProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        messages.success(request,'form valid and saved')
        form.save()
        return redirect('user_profile')
    else:
        messages.success(request,'form invalid')
    return render(request,'authentication/update_profile.html',{'form':form})


def test(request):
    # Profiles=Profile.objects.all()
    # return render(request,'authentication/test.html',{'Profiles':Profiles})
    # help(User)
    # if user.is_authenticated:
    #     print('asaaa')
    print(request.user.profile.pk)
    return redirect('home')

def register_login(request):
    if request.method=='POST':
        if 'register' in request.POST:
            form=UserRegisterForm(request.POST)
            if form.is_valid():
                user=form.save(commit=False)
                user.is_active=False
                user.save()
                email=form.cleaned_data.get('email')
                activateEmail(request,user,email)
                return redirect('home')

        elif 'login' in request.POST:
            username = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, ('login successful'))
                return redirect('all_events')
            else:
                messages.success(request, ('error happen when login, try again or contact admin'))
                return redirect('user_login')

    else:
        form=UserRegisterForm
    return render(request,'authentication/user_register_login.html',{'form':form})
