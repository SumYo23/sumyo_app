from django.urls import path

from cook import api

urlpatterns = [
    path("list/<int:num>/", api.CookList.as_view(), name="cook_list")
]
