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

class Song(models.Model):
	title =  models.CharField(max_length = 50, null = True)

<<<<<<< HEAD
	def __unicode__(self):
		return self.title
=======
=======
class Song(models.Model):
	title =  models.CharField(max_length = 50, null = True)
>>>>>>> c7a0cd3c92aa2a427f8feb60c3763719472c73d5
>>>>>>> cdfcefeaa4e9d5d360fb936e34272fb164a8fc07

class CD(models.Model):
	title = models.CharField(max_length = 100, null = True)
	performer = models.ForeignKey(Performer)
	songs = models.ForeignKey(Song)
	
	def __unicode__(self):
		return self.title
<<<<<<< HEAD

=======
>>>>>>> c7a0cd3c92aa2a427f8feb60c3763719472c73d5
