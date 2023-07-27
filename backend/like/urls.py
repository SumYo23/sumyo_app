from django.urls import path

from .views import LikeCreateView
from .views import LikeDestroyView
from .views import LikeListView

urlpatterns = [
    path('cook_like/', LikeCreateView.as_view(), name="cook-like"),
    path('cook_unlike/<int:like_id>/', LikeDestroyView.as_view(), name="cook-dislike"),
    path('cook_likes/', LikeListView.as_view(), name="cook-list"),
]
