from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from movies.models import Movies
from movies.serializers import MoviesSerializer


class MoviesView(APIView):
    def get(self, request):
        movies = Movies.objects.all()
        serializer = MoviesSerializer(movies, many=True)
        return Response(serializer.data)
