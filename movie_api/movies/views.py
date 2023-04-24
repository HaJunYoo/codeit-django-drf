from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Movie, Actor, Review
from .serializers import MovieSerializer, ActorSerializer, ReviewSerializer


# @api_view(['GET', 'POST'])
# def movie_list(request):
#     # print(request.data)
#     # print(type(request.data))
#     # GET 요청이 들어왔을 때
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     # POST 요청이 들어왔을 때
#     elif request.method == 'POST':
#         # request.data에는 POST 요청으로 들어온 데이터가 들어있습니다.
#         data = request.data
#         serializer = MovieSerializer(data=data)
#         # serializer.is_valid()를 통해 유효성 검사를 진행합니다.
#         # 만약 유효성 검사를 통과하면 save() 함수가 실행되어
#         # MovieSerializer에서 정의했던 create() 함수가 실행되고, Movie 객체가 생성됩니다.
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     return Response(status=status.HTTP_400_BAD_REQUEST)

# class MovieList(APIView):
#     def get(self, request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class MovieDetail(APIView):
#     def get_object(self, pk):
#         # pk에 해당하는 Movie 객체를 가져옵니다.
#         movie = get_object_or_404(Movie, pk=pk)
#         return movie
#
#     def get(self, request, pk):
#         # GET 요청을 처리합니다.
#         movie = self.get_object(pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#
#     def patch(self, request, pk):
#         # PATCH 요청을 처리합니다.
#         movie = self.get_object(pk)
#         serializer = MovieSerializer(movie, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         # 유효성 검사를 통과하지 못했을 때
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         # DELETE 요청을 처리합니다.
#         movie = self.get_object(pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PATCH', 'DELETE'])
# def movie_detail(request, pk):
#     # pk에 해당하는 Movie 객체를 가져옵니다.
#     movie = get_object_or_404(Movie, pk=pk)
#     # request.method에 따라 다른 처리를 합니다.
#     if request.method == 'GET':
#         # MovieSerializer를 통해 Movie 객체를 JSON으로 변환합니다.
#         # 하나의 객체를 변환할 때는 many=True 옵션을 주지 않습니다.
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PATCH':
#         # PATCH는 부분 데이터 수정이기 때문에 partial 옵션을 True로 설정합니다.
#         # PUT일 경우, 모든 데이터를 수정, partial=False
#         serializer = MovieSerializer(movie, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         # 유효성 검사를 통과하지 못했을 때
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         movie.delete()
#         # 데이터가 삭제되면 반환할 데이터가 없기 때문에 상태 코드인 204만 반환
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def actor_list(request):
#     # GET 요청이 들어왔을 때
#     if request.method == 'GET':
#         actor = Actor.objects.all()
#         serializer = ActorSerializer(actor, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     # POST 요청이 들어왔을 때
#     elif request.method == 'POST':
#         # request.data에는 POST 요청으로 들어온 데이터가 들어있습니다.
#         data = request.data
#         serializer = ActorSerializer(data=data)
#         # serializer.is_valid()를 통해 유효성 검사를 진행합니다.
#         # 만약 유효성 검사를 통과하면 save() 함수가 실행되어
#         # MovieSerializer에서 정의했던 create() 함수가 실행되고, Movie 객체가 생성됩니다.
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     return Response(status=status.HTTP_400_BAD_REQUEST)


# class ActorList(APIView):
#     def get(self, request):
#         actors = Actor.objects.all()
#         serializer = ActorSerializer(actors, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ActorSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ActorDetail(APIView):
#     def get_object(self, pk):
#         # pk에 해당하는 Movie 객체를 가져옵니다.
#         actor = get_object_or_404(Actor, pk=pk)
#         return actor
#
#     def get(self, request, pk):
#         # GET 요청을 처리합니다.
#         actor = self.get_object(pk)
#         serializer = ActorSerializer(actor)
#         return Response(serializer.data)
#
#     def patch(self, request, pk):
#         # PATCH 요청을 처리합니다.
#         actor = self.get_object(pk)
#         serializer = ActorSerializer(actor, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         # 유효성 검사를 통과하지 못했을 때
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         # DELETE 요청을 처리합니다.
#         actor = self.get_object(pk)
#         actor.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PATCH', 'DELETE'])
# def actor_detail(request, pk):
#     # pk에 해당하는 Actor 객체를 가져옵니다.
#     actor = get_object_or_404(Actor, pk=pk)
#     # request.method에 따라 다른 처리를 합니다.
#     if request.method == 'GET':
#         # ActorSerializer를 통해 Actor 객체를 JSON으로 변환합니다.
#         # 하나의 객체를 변환할 때는 many=False 옵션을 주지 않습니다.
#         serializer = ActorSerializer(actor)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PATCH':
#         # PATCH는 부분 데이터 수정이기 때문에 partial 옵션을 True로 설정합니다.
#         # PUT일 경우, 모든 데이터를 수정, partial=False
#         serializer = ActorSerializer(actor, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         # 유효성 검사를 통과하지 못했을 때
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         actor.delete()
#         # 데이터가 삭제되면 반환할 데이터가 없기 때문에 상태 코드인 204만 반환
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def review_list(request, pk):
#     # 영화 객체 가져오기
#     movie = get_object_or_404(Movie, pk=pk)
#
#     if request.method == 'GET':
#         # GET 요청일 경우, 해당 영화의 리뷰들을 가져와서 시리얼라이저를 통해 응답
#         reviews = Review.objects.filter(movie=movie)
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         # POST 요청일 경우, 전달된 데이터를 시리얼라이저를 통해 검증하고 저장
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(movie=movie)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieList(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'

    # def get_queryset(self):
    #     return Movie.objects.all()

class ActorList(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ReviewList(ListCreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        movie = get_object_or_404(Movie, pk=self.kwargs.get('pk'))
        return Review.objects.filter(movie=movie)

    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, pk=self.kwargs.get('pk'))
        serializer.save(movie=movie)

# python manage.py runserver
