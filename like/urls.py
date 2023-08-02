from django.urls import path

from .views import LikeList, LikeDetail

urlpatterns = [
    path('list/', LikeList.as_view(), name="like-list"),
    path('', LikeDetail.as_view(), name="like-detail")
]
