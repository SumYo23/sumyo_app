from django.urls import path

from user import api

urlpatterns = [
    path('get_token/', api.GetToken.as_view(), name="GetToken"),
    path('delete_token/', api.DeleteToken.as_view(), name="DeleteToken"),
    path('view/', api.UserView.as_view(), name="UserView"),
]
