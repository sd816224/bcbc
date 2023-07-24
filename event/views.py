
from django.shortcuts import render, redirect
from .models import Event,RSVP_Profile_inter
# from .models import Venue,Event,RSVP_Profile_inter
from .forms import EventForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
import datetime as dt
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

def home(request):
    return render(request,'event/home.html',{})

def under_construction(request):
    return render(request,'event/under_construction.html')
def contact(request):
    return render(request,'event/contact.html',{})

# def all_venues(request):
#     venues=Venue.objects.all()
#     return render(request,'event/all_venues.html',{'venues':venues})

# def add_venue(request):
#     submitted=False
#     if request.method=='POST':
#         form = VenueForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/add_venue?submitted=True')
#     else:
#         form = VenueForm
#         if 'submitted' in request.GET:
#             submitted=True
#     return render(request,'event/add_venue.html',{'form':form,'submitted':submitted})

def update_event(request,event_id):
    event=Event.objects.get(pk=event_id)
    form=EventForm(request.POST or None,request.FILES or None,instance=event)
    if form.is_valid():
        messages.success(request,'form is valid and saved, thanks for the update')
        form.save()
        return redirect('event_detail',event_id)
    # else:
    #     messages.success(request,'form is not valid, please check..')
        print(form.errors)
    return render(request,'event/update_event.html',{'form':form})



def all_events(request):
    alert=False
    if request.method=='POST':
        messages.success(request,'sorry! you can register as a member to view the events')
        return HttpResponseRedirect('/all_events?alert=True')
    else:
        #debug only
        events=Event.objects.all()

        # events=Event.objects.all().filter(event_datetime__range=[dt.datetime.now(),dt.datetime.now()+dt.timedelta(days=90)])

        if 'alert' in request.GET:
            alert=True
    return render(request,'event/all_events.html',{'events':events,'alert':alert})

def event_detail(request,event_id):
    current_profile=request.user.profile
    event=Event.objects.get(pk=event_id)
    attendees = event.rsvp_profile_inter_set.all().order_by('-RSVP_datetime')

    if (current_profile.id,) in attendees.values_list('profile'):
        rsvp_status=True
    else:
        rsvp_status = False

    #debug area
    print(event.organiser.profile.first_name)
    # print(current_profile.event_set.all())
    # print(event.rsvp_profile_inter_set.all().order_by('-RSVP_datetime'))
    # print(current_profile)
    # print(attendees.values_list('profile'))
    # print(rsvp_status)

    if not rsvp_status and request.method=='POST':
        RSVP_Profile_inter.objects.create(
            event=event,
            profile=current_profile,
            RSVP_datetime=dt.datetime.now()
        )
        return HttpResponseRedirect('?rsvp_status=Ture')

    elif rsvp_status and request.method=='POST':
        RSVP_Profile_inter.objects.filter(
            event=event,
            profile=current_profile
        ).delete()

        return HttpResponseRedirect('?rsvp_status=False')

    return render(request,'event/event_detail.html',{'event':event,'rsvp_status':rsvp_status})

def add_event(request):
    submitted=False
    if request.method=='POST':
        # print(request.POST['event_datetime'])

        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            new_event=form.save(commit=False)
            new_event.organiser=request.user
            new_event.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form=EventForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'event/add_event.html',{"form":form,'submitted':submitted})

def send_notification(request):
    if send_mail(
        subject='test subject ',
        message='test message 22',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['bet816224@yahoo.com','luckysportsman456@gmail.com'],
    ) ==1:
        print('email sent')

