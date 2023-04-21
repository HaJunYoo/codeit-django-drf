from django.urls import path
from .views import movie_list, actor_list, review_list, movie_detail, actor_detail

urlpatterns = [
    path('movies', movie_list),
    path('actors', actor_list),
    path('movies/<int:pk>', movie_detail),
    path('actors/<int:pk>', actor_detail),
    path('movies/<int:pk>/reviews', review_list),
]