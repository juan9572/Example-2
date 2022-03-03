import re
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import re_path
from .models import Movie

# Create your views here.

def about(request):
    return HttpResponse('<h1>Welcome to about page</h1>')
    
def movie(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'movie.html', {'name':'Juan Pablo', 'searchTerm':searchTerm, 'movies':movies})