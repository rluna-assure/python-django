from django.urls import path
from . import views

app_name = "movie"
urlpatterns = [
    path("", views.index, name="index" ),
    path("dashboard/", views.my_dashboard, name="dashboard"),
    path("login/", views.my_login, name="login"),
    path("user_login/", views.user_login, name="user_login"),
    path("user_logout/", views.user_logout, name="logout"),
    
    path("genre_list/", views.genre_list_view, name="genre_list"),
    path("actors_list/", views.actor_list_view, name="actors_list"),
    path("movie_list/", views.movie_list_view, name="movie_list"),
    
    path("movie_form/", views.movie_form, name="movie_form"),
    path("genre_form/", views.genre_form, name="genre_form"),
    path("actor_form/", views.actor_form, name="actor_form"),

    path("genre_save/", views.genre_save, name="genre_save"),
    path("movie_save/", views.movie_save, name="movie_save"),
    path("actor_save/", views.actor_save, name="actor_save"),
    
    path('genre/<int:genre_id>/', views.movies_by_genre, name='movies_by_genre'),
    path('actor/<int:actor_id>/', views.movies_by_actor, name='movies_by_actor'),
    
    path("search_list_view/", views.search_list_view, name="search_list_view"),
    
    path('movie/<int:movie_id>/', views.movie_detail_view, name='movie_detail'),
    
    path('movie/<int:movie_id>/like/', views.like_movie, name='like_movie'),
    path('movie/<int:movie_id>/dislike/', views.dislike_movie, name='dislike_movie'),
    
]
