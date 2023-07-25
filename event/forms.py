from django import forms
from django.forms import ModelForm
from .models import Event


# class VenueForm(ModelForm):
#     class Meta:
#         model=Venue
#         fields=('name','address','venue_type','note')
#
#         labels={
#             'name':'',
#             'address':'',
#             'venue_type':'venue type',
#             'note':'',
#         }
#         widgets={
#             'name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter venue name '}),
#             'address':forms.TextInput(attrs={'class':'form-control','placeholder':'enter venue address '}),
#             'venue_type':forms.Select(attrs={'class':'form-control'}),
#             'note':forms.Textarea(attrs={'class':'form-control','placeholder': 'please any note for people who like '
#                                                                                'to go to play '}),
#         }
#

class EventForm(ModelForm):


    event_datetime=forms.DateTimeField(
        widget=forms.DateTimeInput(format='%d/%m/%y %H:%M'),
        input_formats=['%d/%m/%y %H:%M'],
        # help_text='AAAA'
    )
    class Meta:
        model=Event
        fields=(
            'name',
            'event_datetime',
            'duration',
            'organiser',
            'venue',
            'max_players',
            'price',
            'payment_qr',
            'activity_note',
        )
        labels={
            'name': "Event name ",
            # 'event_datetime': "",
            'duration': "Event duration",
            # 'organiser': "Event organiser",
            'venue': "Event address",
            'max_players':"Max number of players",
            'price':"Price",
            'payment_qr':'you can attached wechat payment QR code to take the payment',
            'activity_note': "",
            # 'RSVP':''
        }
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'event name'}),
            'duration':forms.Select(attrs={'class':'form-control'}),
            # 'event_datetime':forms.DateTimeInput(format='%d/%m/%y %H:%M',attrs={'class':'form-control','placeholder':'enter event datetime'}),
            'organiser':forms.HiddenInput(),
            'venue':forms.TextInput(attrs={'class':'form-control'}),
            'max_players':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control','placeholder':'your charge per player'}),
            'activity_note':forms.Textarea(attrs={'class':'form-control','placeholder':'enter any note of event'}),
            # 'RSVP':forms.TextInput(attrs={'class':'sr-only sr-only-focusable','placeholder':'????'}),
        }

    def __init__(self,*args,**kwargs):
        super(EventForm,self).__init__(*args,**kwargs)
        self.fields['event_datetime'].widget.attrs['class']='form-control'
        self.fields['event_datetime'].widget.attrs['placeholder']='event datetime'
        self.fields['event_datetime'].label='please enter the format as DD/MM/YY HH:MM (example: 25/12/23 08:00)'
