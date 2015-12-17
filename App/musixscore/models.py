from django.db import models

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

<<<<<<< HEAD
=======

>>>>>>> 6551e8a759bdaa0216af0dc8c29d0e8f43396648
class Song(models.Model):
	title =  models.CharField(max_length = 50, null = True)
	genre = models.ForeignKey('Genre')
	performer = models.ForeignKey('Performer')

<<<<<<< HEAD
	def __unicode__(self):
		return self.title
=======
<<<<<<< HEAD
=======
<<<<<<< HEAD
	def __unicode__(self):
		return self.title
=======
=======
class Song(models.Model):
	title =  models.CharField(max_length = 50, null = True)
>>>>>>> c7a0cd3c92aa2a427f8feb60c3763719472c73d5
>>>>>>> cdfcefeaa4e9d5d360fb936e34272fb164a8fc07
>>>>>>> 567c3e4096d68ea6eedfad8cd5fa3e1ca06f53e7
>>>>>>> 6551e8a759bdaa0216af0dc8c29d0e8f43396648

class CD(models.Model):
	title = models.CharField(max_length = 100, null = True)
	performer = models.ForeignKey(Performer)
	songs = models.ForeignKey(Song)
	
	def __unicode__(self):
		return self.title
<<<<<<< HEAD
=======

>>>>>>> 6551e8a759bdaa0216af0dc8c29d0e8f43396648
