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
>>>>>>> 0ed92d4c94a19a5398b6027d820e2d17a3c980f4
class Song(models.Model):
	title =  models.CharField(max_length = 50, null = True)
	genre = models.ForeignKey('Genre')
	performer = models.ForeignKey('Performer')

	def __unicode__(self):
		return self.title
<<<<<<< HEAD

=======
>>>>>>> 0ed92d4c94a19a5398b6027d820e2d17a3c980f4

class CD(models.Model):
	title = models.CharField(max_length = 100, null = True)
	performer = models.ForeignKey(Performer)
	songs = models.ForeignKey(Song)
	
	def __unicode__(self):
		return self.title
<<<<<<< HEAD

=======
>>>>>>> 0ed92d4c94a19a5398b6027d820e2d17a3c980f4
