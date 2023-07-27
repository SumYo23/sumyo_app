from django.urls import path

from cook import views

urlpatterns = [
    path("list/<int:num>/", views.CookList.as_view(), name="cook_list")
]
