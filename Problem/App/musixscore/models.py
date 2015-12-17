from django.db import models

# Create your models here.
class CD(models.Model):
	title = models.CharField(max_length=300)
	# songs = models.ForeignKey(Song)

	def __unicode__(self):
		return self.title

