from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Movie, Actor
from .serializers import MovieSerializer, ActorSerializer


@api_view(['GET', 'POST'])
def movie_list(request):
    # GET 요청이 들어왔을 때
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # POST 요청이 들어왔을 때
    elif request.method == 'POST':
        # request.data에는 POST 요청으로 들어온 데이터가 들어있습니다.
        data = request.data
        serializer = MovieSerializer(data=data)
        # serializer.is_valid()를 통해 유효성 검사를 진행합니다.
        # 만약 유효성 검사를 통과하면 save() 함수가 실행되어
        # MovieSerializer에서 정의했던 create() 함수가 실행되고, Movie 객체가 생성됩니다.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def actor_list(request):
    # GET 요청이 들어왔을 때
    if request.method == 'GET':
        actor = Actor.objects.all()
        serializer = ActorSerializer(actor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # POST 요청이 들어왔을 때
    elif request.method == 'POST':
        # request.data에는 POST 요청으로 들어온 데이터가 들어있습니다.
        data = request.data
        serializer = ActorSerializer(data=data)
        # serializer.is_valid()를 통해 유효성 검사를 진행합니다.
        # 만약 유효성 검사를 통과하면 save() 함수가 실행되어
        # MovieSerializer에서 정의했던 create() 함수가 실행되고, Movie 객체가 생성됩니다.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)