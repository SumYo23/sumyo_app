from django.urls import path

from .views import LikeCreateView, LikeList, LikeDetail
from .views import LikeDestroyView
from .views import LikeListView

urlpatterns = [
    path('cook_like/', LikeCreateView.as_view(), name="cook-like"),
    path('cook_unlike/<int:cook_id>/', LikeDestroyView.as_view(), name="cook-dislike"),
    path('cook_likes/', LikeListView.as_view(), name="cook-list"),
    path('list/', LikeList.as_view(), name="like-list"),
    path('', LikeDetail.as_view(), name="like-detail")
]
