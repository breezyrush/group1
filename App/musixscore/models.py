from django.db import models

# Create your models here.
class Genre(models.Model):
	genre = models.CharField(max_length = 50)


class Performer(models.Model):
	fname = models.CharField(max_length = 50, null = True)
	lname = models.CharField(max_length = 50, null = True)
	gender =  models.CharField(max_length = 50, null = True)
	age = models.PositiveIntegerField(default = 0)
