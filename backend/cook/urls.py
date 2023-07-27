from django.urls import path

from cook import views

urlpatterns = [
    path("list/<int:num>/", views.CookList.as_view(), name="cook_list"),  # 추천 요리 목록
    #path("list/<int:num>/likes/", views.LikeList.as_view(), name="like_list"),  # 찜 목록
    path("ingredient/list/", views.IngredientList.as_view(), name="ingredient_list"),  # db전체 재료 목록
]
