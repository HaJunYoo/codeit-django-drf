from rest_framework import serializers
from .models import Movie, Actor


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    opening_date = serializers.DateField()
    running_time = serializers.IntegerField()
    overview = serializers.CharField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)


# 여기에 코드를 작성하세요
class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=10)
    gender = serializers.CharField(max_length=1)
    birth_date = serializers.DateField()

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)