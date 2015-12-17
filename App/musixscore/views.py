from django.shortcuts import render

def browse(request):
	genre = request.GET.get('genre', '')
	performer = request.GET.get('performer', '')
	cd = request.GET.get('cd','')
	

	return render(request, 'browse/browse.html', {})