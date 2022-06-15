from django.urls import path,include
from app.watchlist.api.views import (
    watch_list,
    watch_detail,
    stream_platform_list,
    stream_platform_detail,
    review_list,
    review_detail
)

urlpatterns =[
    path('list', watch_list,name='watch-list'),
    path('<int:pk>', watch_detail,name='watch-detail'),
    path('stream/',stream_platform_list,name='streamlist'),
    path('stream/<int:pk>',  stream_platform_detail,name='streamplatform-detail'),
    path('review', review_list ,name='review-list'),
    path('review/<int:pk>', review_detail ,name='review-detail'),
    # path('stream/<int:pk>/review', review_detail ,name='review-detail'),
]