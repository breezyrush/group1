from django.shortcuts import render
from .models import *

def browse(request):
	genre = request.GET.get('genre', '')
	performer = request.GET.get('performer', '')
	cd = request.GET.get('cd','')

	if request.method == 'POST':
		songs = request.POST.getlist('songs[]')

	genre_list = Genre.objects.all()

	performer_list = []
	cd_list = []
	songs_list = []

	if not genre == '':
		performer_list = Performer.objects.all().filter(genre=genre)

	if not genre == '' and not performer == '':
		 cd_list = CD.objects.all().filter(performer=performer)

	if not genre == '' and not performer == '' and not cd == '':
		songs_list = Song.objects.all().filter(cd=cd)

	if not cd == '':
		cd_list = CD.objects.all().filter(performer=performer)

	return render(request, 'browse/browse.html', {
		'genre_list': genre_list,
		'performer_list' : performer_list,
		'cd_list': cd_list, 
		'songs': songs_list,

		'genre' : genre,
		'performer' : performer,
		'cd': cd,
	})
