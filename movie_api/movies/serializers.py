from rest_framework import serializers
from rest_framework.serializers import ValidationError
from django.core.validators import MaxLengthValidator, MinLengthValidator
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from .models import Movie, Actor, Review


# Movie 모델에 존재하는 모든 필드와 create() 함수가 정의
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     opening_date = serializers.DateField()
#     running_time = serializers.IntegerField()
#     overview = serializers.CharField()
#
#     # create()를 통해 serializer.save()가 실행되면 새로운 데이터가 생성
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     # 수정 요청이 들어온 필드만 validated_data로 수정하고, 나머지는 기존의 값을 그대로 사용
#     # get을 통해 구현 -> validated_data에 값이 존재한다면 수정 요청한 값을, 없다면 기존 필드 값(instance.name)을 넣고 데이터를 수정
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.opening_date = validated_data.get('opening_date', instance.opening_date)
#         instance.running_time = validated_data.get('running_time', instance.running_time)
#         instance.overview = validated_data.get('overview', instance.overview)
#         instance.save()
#         return instance

def overview_validator(value):
    if value > 300:
        raise ValidationError('소개 문구는 최대 300자 이하로 작성해야 합니다.')
    elif value < 10:
        raise ValidationError('소개 문구는 최소 10자 이상으로 작성해야 합니다.')
    return value


class MovieSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(validators=[UniqueValidator(
    #     queryset=Movie.objects.all(),
    #     message='이미 존재하는 영화 이름입니다.',
    # )])
    # validators using function
    # overview = serializers.CharField(validators=[overview_validator])
    # pk related field
    # movie_reviews = serializers.PrimaryKeyRelatedField(source='reviews', many=True, read_only=True)
    # string related field
    # reviews = serializers.StringRelatedField(many=True)
    # nested serializer
    # reviews = ReviewSerializer(many=True, read_only=True)
    actors = serializers.StringRelatedField(many=True, read_only=True)


    class Meta:
        model = Movie
        fields = ['id', 'name', 'reviews','actors','opening_date', 'running_time', 'overview']
        validators = [
            UniqueTogetherValidator(
                queryset=Movie.objects.all(),
                fields=['name', 'overview'],
            )
        ]
        read_only_fields = ['reviews', 'actors']

    def validate(self, attrs):
        if 10 > len(attrs['overview']) or len(attrs['overview']) > 300:
            raise ValidationError('영화 소개는 10자 이상, 300자 이하로 작성해주세요.')
        if len(attrs['name']) > 50:
            raise ValidationError('영화 이름은 50자 이하로 작성해주세요.')
        return attrs


class ReviewSerializer(serializers.ModelSerializer):
    # movie = serializers.StringRelatedField()
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'movie', 'username', 'star', 'comment', 'created']
        extra_kwargs = {
            'movie': {'read_only': True},
        }

# 여기에 코드를 작성하세요
# class ActorSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=10)
#     gender = serializers.CharField(max_length=1)
#     birth_date = serializers.DateField()
#
#     def create(self, validated_data):
#         return Actor.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.opening_date = validated_data.get('gender', instance.gender)
#         instance.running_time = validated_data.get('birth_date', instance.birth_date)
#         instance.save()
#         return instance
class ActorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = ['id', 'name', 'gender', 'birth_date', 'movies']
        read_only_fields = ['movies']



