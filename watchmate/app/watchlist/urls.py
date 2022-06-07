from django.urls import path,include
from app.watchlist.views import moive_list,movie_detail

urlpatterns =[
    path('list', moive_list,name='movie-list'),
    path('<int:pk>', movie_detail,name='movie-number'),
]