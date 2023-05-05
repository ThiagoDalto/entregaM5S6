from rest_framework import serializers
from .models import Movie
from genres.models import Genre
from genres.serializers import GenreSerializer


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model: Movie
        fields = [
            "id",
            "title",
            "duration",
            "premiere",
            "budget",
            "overview",
            "user",

        ]
