from django.shortcuts import render
from django.views.generic import ListView
from photo.models import Album


# Create your views here.
class AlbumLV(ListView):
    model = Album