from django.db import models

<<<<<<< HEAD
class Genre(models.Model):
	genre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.genre
=======
# Create your models here.
<<<<<<< HEAD
class CD(models.Model):
	title = models.CharField(max_length=300)
	# songs = models.ForeignKey(Song)
=======
class Song(models.Model):
	title = models.CharField( max_length = 50 , null = True )
	# genre =
	# performer = 
>>>>>>> d1989efc6bd6d5df523d2ff608414c60efa21fec

	def __unicode__(self):
		return self.title
>>>>>>> d1989efc6bd6d5df523d2ff608414c60efa21fec

