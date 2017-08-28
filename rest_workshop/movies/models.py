from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=128)


class Movies(models.Model):
   title = models.CharField(max_length=64)
   description = models.TextField()
   director = models.ForeignKey(Person, blank=True, null=True)
   actors = models.ManyToManyField(
       Person,
       through="MoviesStarringPerson",
       related_name="movie_person"

   )
   year = models.IntegerField(max_length=4, blank=True, null=True)

class MoviesStarringPerson(models.Model):
    starring_movie = models.ForeignKey(Movies)
    starring_person = models.ForeignKey(Person, related_name="person_name")
    role = models.CharField(max_length=128, blank=True, null=True)