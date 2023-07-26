from django.urls import path

from cook import api
from .views import RecipeListAPIView

urlpatterns = [
    path('recipes/', RecipeListAPIView.as_view(), name="recipe-list"),
    path("list/", api.CookList.as_view(), name="cook_list")
]
