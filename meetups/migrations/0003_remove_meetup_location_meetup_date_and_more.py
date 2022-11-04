# Generated by Django 4.1.3 on 2022-11-04 13:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0002_location_participant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meetup',
            name='location',
        ),
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='meetup',
            name='description',
            field=models.TextField(default='dejaklfkl'),
        ),
        migrations.AddField(
            model_name='meetup',
            name='image',
            field=models.ImageField(default='jadfklaskl', upload_to='images'),
        ),
        migrations.AddField(
            model_name='meetup',
            name='organizer_email',
            field=models.EmailField(default='markos@gm.ion', max_length=254),
        ),
        migrations.AddField(
            model_name='meetup',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, to='meetups.participant'),
        ),
        migrations.AddField(
            model_name='participant',
            name='name',
            field=models.CharField(default='markos', max_length=100),
        ),
        migrations.AlterField(
            model_name='meetup',
            name='slug',
            field=models.SlugField(default='slug'),
        ),
        migrations.AlterField(
            model_name='meetup',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]