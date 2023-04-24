from django.urls import path
# from .views import movie_list, actor_list, movie_detail, actor_detail, review_list
from .views import MovieList, ActorList, MovieDetail, ActorDetail, ReviewList, RetrieveUpdateDestroyAPIView

urlpatterns = [
    path('movies', MovieList.as_view()),
    path('actors', ActorList.as_view()),
    path('movies/<int:pk>', MovieDetail.as_view()),
    path('actors/<int:pk>', ActorDetail.as_view()),
    path('movies/<int:pk>/reviews', ReviewList.as_view()),
    path('movies/<str:name>', RetrieveUpdateDestroyAPIView.as_view())

    # path('movies/<int:pk>', movie_detail),
    # path('actors/<int:pk>', actor_detail),
    # path('movies/<int:pk>/reviews', review_list),
]