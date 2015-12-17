from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Genre(models.Model):
	genre = models.CharField(max_length = 50)

	def __unicode__(self):
		return self.genre

class Performer(models.Model):
	fname = models.CharField(max_length = 50, null = True)
	lname = models.CharField(max_length = 50, null = True)
	gender =  models.CharField(max_length = 50, null = True)
	age = models.PositiveIntegerField(default = 0)	
	genre = models.ForeignKey(Genre)

	def __unicode__(self):
		return self.fname

class CD(models.Model):
	title = models.CharField(max_length = 100, null = True)
	performer = models.ForeignKey(Performer)
	
	def __unicode__(self):
		return self.title

class Song(models.Model):
	title =  models.CharField(max_length = 50, null = True)
	cd = models.ForeignKey(CD)

	def __unicode__(self):
		return self.title

class Cart(models.Model):
	song = models.ForeignKey(Song)
	date = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return self.song