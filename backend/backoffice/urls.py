'''django'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.import_csv, name="import_csv")
]
