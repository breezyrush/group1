from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

def home(request):
	return HttpResponseRedirect(reverse('browse'))
	 
def clear(request):
	cart = Cart.objects.all()
	for c in cart:
		c.delete()
	return HttpResponseRedirect(reverse('browse'))

def browse(request):
	genre = request.GET.get('genre', '')
	performer = request.GET.get('performer', '')
	cd = request.GET.get('cd','')

	if request.method == 'POST':
		songs = request.POST.getlist('songs')
		for song in songs:
			song = Song.objects.get(pk=song)
			i = Cart(song=song)
			i.save()

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

	cart = Cart.objects.all()
	return render(request, 'browse/browse.html', {
		'genre_list': genre_list,
		'performer_list' : performer_list,
		'cd_list': cd_list, 
		'songs_list': songs_list,

		'genre' : genre,
		'performer' : performer,
		'cd': cd,
		'cart': cart, 
	})
