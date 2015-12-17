from django.db import models

class Genre(models.Model):
	genre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.genre

