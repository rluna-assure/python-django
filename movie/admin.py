from django.contrib import admin

from .models import Actor, Tag, Movie, Genre, RateMovieUser, ActorMovie, Image, TagMovie

class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']
    
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']
    
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name','synopsis','duration','year','imdb','trailerLink','genre']
    search_fields = ['name','synopsis','duration','year','imdb','trailerLink','genre']
    list_filter = ['name','synopsis','duration','year','imdb','trailerLink','genre']
    
class ActorAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'age']
    search_fields = ['name', 'last_name', 'age']
    list_filter = ['name', 'last_name', 'age']
    
class ImageAdmin(admin.ModelAdmin):
    list_display = ['image', 'movie']
    search_fields = ['image', 'movie']
    list_filter = ['image', 'movie']
    
class RateMovieUserAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user']
    search_fields = ['movie', 'user']
    list_filter = ['movie', 'user']
    
class ActorMovieAdmin(admin.ModelAdmin):
    list_display = ['actor', 'movie']
    search_fields = ['actor', 'movie']
    list_filter = ['actor', 'movie']
    
class TagMovieAdmin(admin.ModelAdmin):
    list_display = ['tag', 'movie']
    search_fields = ['tag', 'movie']
    list_filter = ['tag', 'movie']

admin.site.register(Tag, TagsAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(TagMovie, TagMovieAdmin)
admin.site.register(RateMovieUser, RateMovieUserAdmin)
admin.site.register(ActorMovie, ActorMovieAdmin)