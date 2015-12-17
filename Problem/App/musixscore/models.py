from django.db import models

<<<<<<< HEAD
# Create your models here.
class Performer(models.Model):
	fname = models.CharField(max_length = 50, null = True)
	lname = models.CharField(max_length = 50, null = True)
	gender =  models.CharField(max_length = 50, null = True)
	age = models.PositiveIntegerField(default = 0)	

	def __unicode__(self):
		return self.name
=======

class Genre(models.Model):
	genre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.genre

class CD(models.Model):
	title = models.CharField(max_length=300)
	# songs = models.ForeignKey(Song)

class Song(models.Model):
	title = models.CharField( max_length = 50 , null = True )
	# genre =
	# performer = 

	def __unicode__(self):
		return self.title

>>>>>>> 6f486dd87d00bfd6e886577d81488369f87cbb0c
