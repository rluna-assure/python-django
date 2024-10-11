from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from ..models import Actor

@login_required
def actor_form(request):
    return render(request, 'movie/actor_form.html')

def actor_list_view(request):
    actors = Actor.objects.all()
    data = set_data("actors", actors)
    return render(request, 'movie/actor_list.html', data)

def set_data(name, data):
    context= {
        name: data
    }
    return context

@login_required
def actor_save(request):
    name = request.POST['name']
    last_name = request.POST['last_name']
    age = request.POST['age']
    actor = Actor(name=name, last_name=last_name, age=age)
    actor.save()

    return redirect("movie:actors_list")
