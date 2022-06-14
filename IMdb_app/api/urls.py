from django.contrib import admin
from django.db import router
from django.urls import path, include
from .views import StreamingPlatform, StreamPlatform_Detail, watchlistAV, watchlistDetailAV, ReviewList, ReviewDetail, AddReview
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('stream', StreamingPlatform.as_view(), basename='streamplatform')

urlpatterns = [
    # path('list/', views.movie_list, name = 'movie_list'),
    # path('<int:pk>', views.movie_detail, name = 'movie-detail'),
    path('watchlist/', watchlistAV.as_view() , name = 'movie_list'),
    path('watchlist/<int:pk>', watchlistDetailAV.as_view(), name = 'movie-detail'),
    path('platformlist/', StreamingPlatform.as_view(), name = 'StreamPlatform' ),
    path('platformlist/<int:pk>', StreamPlatform_Detail.as_view(), name = 'StreamPlatform-dteail' ),

    path('<int:pk>/reviews', ReviewList.as_view(), name = 'reviewlist'),   #gives review of a specific movie
    path('reviews/<int:pk>', ReviewDetail.as_view(), name = 'review-detail'),  #gives detail of a specific review
    path('<int:pk>/addreview', AddReview.as_view(), name= 'add-review'),


#   path('', include(router.urls)),     router url example

]

