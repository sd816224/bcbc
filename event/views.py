from django.shortcuts import render, redirect
from .models import Venue,Event,RSVP_Profile_inter
# from .models import Venue,Event,RSVP_Profile_inter
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
import datetime

# Create your views here.

def home(request):
    return render(request,'event/home.html',{})

def contact(request):
    return render(request,'event/contact.html',{})

def all_venues(request):
    venues=Venue.objects.all()
    return render(request,'event/all_venues.html',{'venues':venues})

def add_venue(request):
    submitted=False
    if request.method=='POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'event/add_venue.html',{'form':form,'submitted':submitted})

def update_event(request,event_id):
    event=Event.objects.get(pk=event_id)
    form=EventForm(request.POST or None,request.FILES or None,instance=event)
    if form.is_valid():
        messages.success(request,'form is valid and saved, thanks for the update')
        form.save()
        return redirect('all_events')
    # else:
    #     messages.success(request,'form is not valid, please check..')
        print(form.errors)
    return render(request,'event/update_event.html',{'form':form})



def all_events(request):
    # events=Event.objects.all()
    events=Event.objects.all().filter(event_datetime__range=[datetime.datetime.now(),datetime.datetime.now()+datetime.timedelta(days=90)])
    print(datetime.datetime.now())
    print(datetime.datetime.now()+datetime.timedelta(days=90))
    return render(request,'event/all_events.html',{'events':events})

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
            RSVP_datetime=datetime.datetime.now()
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
        print(request.POST['event_datetime'])

        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form=EventForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'event/add_event.html',{"form":form,'submitted':submitted})
