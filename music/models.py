from django.db import models

class Album(models.Model):
	artist = models.CharField(max_length=30)
	album_title=models.CharField(max_length=500)
	genre = models.CharField(max_length=100)
	album_logo = models.CharField(max_length=100)

	def __str__(self):
		return ("<br>" + self.artist + "<br><nr>")

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	file_type = models.CharField(max_length=10)
	song_title = models.CharField(max_length=250)

	def __str__(self):
		return self.song_title
