from django.db import models

class UploadVideo(models.Model):
	title 	  = models.CharField(max_length=100)
	vid   	  = models.FileField()
	snippet   = models.CharField(max_length=100)
	thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)

	def __str__(self):
		return self.title
