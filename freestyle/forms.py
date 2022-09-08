from django import forms
from django.forms import ModelForm
from .models import UploadSong

class UploadSongForm(forms.ModelForm):
	class Meta:
		model = UploadSong
		fields = ('__all__')

