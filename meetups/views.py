from django.shortcuts import render
from meetups.models import Meetup

def index(request):
    meetups=Meetup.objects.all()
    data = {
        'meetups': meetups
    }
    return render(request,'meetups/includes/index.html',data)
def meetup_details(request,meetup_id):

    selected_meetup = Meetup.objects.get(id=meetup_id)
    
    data = {
            'meetup_found': True,
            'meetup': selected_meetup,
                }
    return render(request, 'meetups/includes/meetup_detail.html', data)
