'''django'''
from django.urls import path
from . import views
from .views import ImageDetaction

urlpatterns = [
    path('', ImageDetaction.as_view(), name="api_ai")
]
