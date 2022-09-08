from django.shortcuts import render, redirect
from .models import UploadSong
from .forms import UploadSongForm

def freestyle_index(request):
	songs = UploadSong.objects.all()
	context = {
		'songs':songs
	}
	return render(request, "freestyle/index.html", context)


def upload_song(request):
	form = UploadSongForm()
	if request.method == "POST":
		form = UploadSongForm(data=request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect("freestyle_index")
	else:
		form = UploadSongForm()

	context = {
		'form':form
	}
	return render(request, "freestyle/upload_song.html", context)