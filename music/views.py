from django.shortcuts import render, get_object_or_404, redirect
from .models import UploadVideo
from .forms import UploadVidForm

def index(request):
	vids = UploadVideo.objects.all()

	context = {
		'vids':vids
	}
	return render(request, "music/index.html", context)


def detail(request, id):
	vid = get_object_or_404(UploadVideo, pk=id)
	more_vids = UploadVideo.objects.all()
	context = {
		'vid':vid,
		'more_vids':more_vids
	}
	return render(request, "music/detail.html", context)

def about(request):
	return render(request, "music/about.html")

def upload_vid(request):
	form = UploadVidForm()
	if request.method == "POST":
		form = UploadVidForm(data=request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect("/")
	else:
		form = UploadVidForm()

	context = {
		'form':form
	}
	return render(request, "music/upload_vid.html", context)