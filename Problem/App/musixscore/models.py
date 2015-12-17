from django.db import models

# Create your models here.
class Song(models.Model):
	title = models.CharField( max_length = 50 , null = True )
	# genre =
	# performer = 

	def __unicode__(self):
		return self.title

