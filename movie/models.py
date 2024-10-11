from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Actor(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=100)
    synopsis = models.CharField(max_length=250)
    duration = models.IntegerField()
    year = models.IntegerField()
    imdb = models.FloatField()
    trailerLink = models.CharField(max_length=250)
  
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class RateMovieUser(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reaction = models.CharField(max_length=10, choices=[('like', 'Like'), ('dislike', 'Dislike')])
    
    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f"{self.user.username} - {self.movie.name} - {self.reaction}"

class ActorMovie(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class TagMovie(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Image(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    