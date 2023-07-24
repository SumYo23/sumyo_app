from django.urls import path

from user import api

urlpatterns = [
    path('register/', api.RegisterView.as_view(), name="RegisterView"),
    path('login/', api.LoginView.as_view(), name="LoginView"),
    path('view/', api.UserView.as_view(), name="UserView"),

]
