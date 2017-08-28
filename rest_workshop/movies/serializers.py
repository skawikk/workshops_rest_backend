from rest_framework import serializers

from .models import Movies, Person, MoviesStarringPerson


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ["title", "description", "director", "actors", "year"]


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["name"]


class MobiesStarringPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoviesStarringPerson
        fields = ["starring_movie", "starring_person", "role"]
