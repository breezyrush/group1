from django.shortcuts import render
from .models import *
from .admin import *

def browse(request):
	genre = Genre.objects.all()

	return render(request, 'browse/browse.html', {})