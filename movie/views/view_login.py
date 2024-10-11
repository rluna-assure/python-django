from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count, Q
from ..models import Movie, Genre, Actor, RateMovieUser

def my_login(request):
    return render(request, 'movie/login.html')

def my_dashboard(request):
    return render(request, 'movie/dashboard.html')

def user_login(request):
    username = request.POST["username"]
    password = request.POST["password"]

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("movie:index")
    else:
        context = {
            "error_message": "Nombre de usuario o contraseña incorrectos."
        }
        return render(request, 'movie:login', context)

def user_logout(request):
    logout(request)
    return redirect('movie:index')

def index(request):
    movies = (Movie.objects
              .prefetch_related('genre', 'actormovie_set', 'image_set')
              .annotate(
                  like_count=Count('ratemovieuser', filter=Q(ratemovieuser__reaction='like')),
                  dislike_count=Count('ratemovieuser', filter=Q(ratemovieuser__reaction='dislike'))
              )
              .all())
    genres = Genre.objects.all()
    actors = Actor.objects.all()
    user_reactions=[]
    if request.user.is_authenticated:
     user_reactions = {reaction.movie.id: reaction.reaction for reaction in RateMovieUser.objects.filter(user=request.user)}
    
    context = {
        'genres': genres,
        'movies': movies,
        'actors': actors,
        'user_reactions': user_reactions,
    }
    return render(request, 'movie/index.html',context)

def movie_list_view(request):
    movies = (Movie.objects
              .prefetch_related('genre', 'actormovie_set', 'image_set')
              .annotate(like_count=Count('ratemovieuser', filter=Q(ratemovieuser__reaction='like')))
              .all())
    genres = Genre.objects.all()

    context = {
        'movies': movies,
        'genres': genres,
    }
    return render(request, 'movie/movie_list.html', context)

def movies_by_genre(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    movies = Movie.objects.filter(genre=genre)

    context = {
        'genre': genre,
        'movies': movies,
    }
    return render(request, 'movie/movies_by_genre.html', context)

def movies_by_actor(request, actor_id):
    actor = Actor.objects.get(id=actor_id)
    movies = Movie.objects.filter(actormovie__actor=actor)

    context = {
        'actor': actor,
        'movies': movies,
    }
    return render(request, 'movie/movies_by_actor.html', context)

def movie_detail_view(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    images = movie.image_set.all()
    actors = movie.actormovie_set.all()

    context = {
        'movie': movie,
        'images': images,
        'actors': actors,
    }

    return render(request, 'movie/movie_detail.html', context)

def like_movie(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, id=movie_id)
        RateMovieUser.objects.update_or_create(
            user=request.user,
            movie=movie,
            defaults={'reaction': 'like'}
        )
    return redirect('movie:index')

def dislike_movie(request, movie_id):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, id=movie_id)
        RateMovieUser.objects.update_or_create(
            user=request.user,
            movie=movie,
            defaults={'reaction': 'dislike'}
        )
    return redirect('movie:index')
