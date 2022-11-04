from django.shortcuts import render
from meetups.models import Meetup

def index(request):
    meetups=Meetup.objects.all()
    data = {
        'meetups': meetups
    }
    return render(request,'meetups/includes/index.html',data)
