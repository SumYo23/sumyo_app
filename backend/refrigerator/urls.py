from django.urls import path

from refrigerator import api

urlpatterns = [
    path('ingredient_list/', api.IngredientList.as_view(), name="IngredientList"),
    path('ingredient_list/<int:name>', api.IngredientList.as_view(), name="IngredientList"),
]
