from django import forms
from django.forms import ModelForm
from .models import UploadVideo

class UploadVidForm(forms.ModelForm):
	class Meta:
		model = UploadVideo
		fields = ("__all__")