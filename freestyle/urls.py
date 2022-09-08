from django.urls import path
from . import views


urlpatterns = [
	path('', views.freestyle_index, name="freestyle_index"),
	path('upload/', views.upload_song, name="freestyle_upload"),
]