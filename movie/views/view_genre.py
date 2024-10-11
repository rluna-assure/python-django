from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from ..models import Genre

@login_required
def genre_form(request):
    return render(request, 'movie/genre_form.html')

@login_required
def genre_save(request):
    name = request.POST['name']
    genre = Genre(name=name)
    genre.save()

    return redirect("movie:genre_list")

def genre_list_view(request):
    genres = Genre.objects.all()
    data = set_data("genres", genres)
    return render(request, 'movie/genre_list.html', data)

def set_data(name, data):
    context= {
        name: data
    }
    return context