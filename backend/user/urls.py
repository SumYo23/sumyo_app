from django.urls import path

from user import api

urlpatterns = [
    path('get_token/', api.GetToken.as_view(), name="GetToken"),
]
