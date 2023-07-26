from django.urls import path

from .views import LikeCreateView
from .views import LikeDestroyView

urlpatterns = [
    path('cook_like/', LikeCreateView.as_view(), name="cook-like"),
    path('cook_unlike/<int:like_id>/', LikeDestroyView.as_view(), name="cook-dislike"),
]
