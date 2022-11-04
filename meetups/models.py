from django.db import models
from django.utils import timezone
# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name

class Participant(models.Model):
    name = models.CharField(max_length=100, default='markos')
    email = models.EmailField(unique=True)

    def __str__(self):

        return self.name
        

class Meetup(models.Model):
    
    title = models.CharField(max_length=200)
    organizer_email = models.EmailField(default='markos@gm.ion')
    date = models.DateField(default = timezone.now)
    slug = models.SlugField( default='slug')
    description = models.TextField(default='dejaklfkl')
    image = models.ImageField(upload_to='images', default='jadfklaskl')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participants = models.ManyToManyField(Participant, blank=True, null=True)

    def __str__(self):

        return self.title