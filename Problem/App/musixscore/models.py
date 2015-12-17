from django.db import models


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

