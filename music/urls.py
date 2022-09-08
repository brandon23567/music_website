from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('<int:id>/', views.detail, name="detail"),
	path('about/', views.about, name="about"),
	path('upload_vid/', views.upload_vid, name="upload_vid"),
]