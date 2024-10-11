from django.shortcuts import render
from django import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from ..models import Movie, Genre, Image, Actor, ActorMovie

def movies(request):
    movies = Movie.objects.all()
    
    context = {
        "movies": movies
    }
    
    return (render, "movie/movies", context)

@login_required
def save_movie(request):
    return redirect("movie:index")

@login_required
def movie_form(request):
    genres = Genre.objects.all()
    actors = Actor.objects.all() 
    
    context = {
        "genre_list" : genres,
        "actor_list": actors
    }

    return render(request, 'movie/movie_form.html', context)

def movie_list_view(request):
    movies = Movie.objects.all()
    data = set_data("movies", movies)
    return render(request, 'movie/movie_list.html', data)

def set_data(name, data):
    context= {
        name: data
    }
    return context

@login_required
def movie_save(request):
    name = request.POST['name']
    synopsis = request.POST['synopsis']
    duration = request.POST['duration']
    year = request.POST['year']
    imdb = request.POST['imdb']
    trailerLink = request.POST['trailerLink']
    genre_id = request.POST['genre']
    
    if genre_id =='':
        context["error_message"] = "El genero es obligatorio"
        return render(request, "movie/movie_form.html", context)
    
    if name =='':
        context["error_message"] = "El nombre es obligatorio"
        return render(request, "movie/movie_form.html", context)
    
    genre = Genre.objects.get(pk=genre_id)
    
    movie = Movie(
        name = name, 
        synopsis = synopsis,
        duration = duration, 
        year = year,
        imdb = imdb,
        genre = genre,
        trailerLink = trailerLink
    )
    
    images = request.FILES.getlist('images')
    actor_ids = request.POST.getlist('actors')
    if len(images) < 1:
        context = {"error_message": "Debes minimo 1 imágen.", "genre_list": Genre.objects.all()}
        return render(request, "movie/movie_form.html", context)
    
    movie.save() 
    
    for img in images:
        Image.objects.create(movie=movie, image=img)
    
    for actor_id in actor_ids:
        actor = Actor.objects.get(pk=actor_id)
        ActorMovie.objects.create(actor=actor, movie=movie)

    return redirect("movie:movie_list")

def search_list_view(request):
    query = request.GET.get('q')
    movies = Movie.objects.all()
    genres = Genre.objects.all()
    actors = Actor.objects.all()

    if query:
        movies = movies.filter(name__icontains=query)
        movies_by_genre = Movie.objects.filter(genre__name__icontains=query)
        movies_by_actor = Movie.objects.filter(actormovie__actor__name__icontains=query)
        
        movies = movies | movies_by_genre | movies_by_actor
    
    movies = movies.distinct()
    
    context = {
        'genres': genres,
        'movies': movies,
        'actors': actors,
    }
    
    return render(request, 'movie/index.html', context)    