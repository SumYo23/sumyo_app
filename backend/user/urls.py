from django.urls import path
from . import views
from .views import SignupView

urlpatterns = [
    path('', SignupView.as_view(), name="SignupView")
]
