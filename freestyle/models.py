from django.db import models

class UploadSong(models.Model):
	song = models.FileField(upload_to="songs/")
	song_name = models.CharField(max_length=100)

	def __str__(self):
		return self.song_name
