from django.contrib import admin

from meetups.models import Location, Meetup, Participant

class LocationAdmin(admin.ModelAdmin):

    list_display = ['name', 'address']

admin.site.register(Location, LocationAdmin)

class MeetupAdmin(admin.ModelAdmin):

    list_display = ['title', 'organizer_email','date']

admin.site.register(Meetup, MeetupAdmin)

class ParticipantAdmin(admin.ModelAdmin):

    list_display = ['name', 'email']

admin.site.register(Participant, ParticipantAdmin)