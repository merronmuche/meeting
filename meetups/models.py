from django.db import models

# Create your models here.

class Meetup(models.Model):
    
    title=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    slug=models.CharField(max_length=100)