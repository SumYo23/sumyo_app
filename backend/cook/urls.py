from django.urls import path

from cook import api

urlpatterns = [
    path('recipe_list/', api.RecipeList.as_view(), name="RecipeList"),
]
