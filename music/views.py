from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Album

def index(req):
	all = Album.objects.all()
	#html = ''
	#for album in all:
	#	url = '/music/'+str(album.id)+'/'
	#	html += '<a href="' + url +'">'+album.album_title + '</a><br>'
	## template = loader.get_template('music/index.html')
	##context = { 'all_albums': all}
	##return HttpResponse(template.render(context, req))
	return render(req, 'music/index.html', { 'all_albums': all})

def detail(req, album_id):
	#try:
	#	album = Album.objects.get(pk=album_id)
	#except Album.DoesNotExist:
	#	raise Http404("Album does not exist")
	album = get_object_or_404(Album, pk=album_id)

	context = {
		'album_id': album_id,
		'album':album
	}
	return render(req, 'music/detail.html', context)
