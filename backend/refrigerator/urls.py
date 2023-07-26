from django.urls import path

from refrigerator import api

urlpatterns = [
    path('list/', api.RefrigeratorList.as_view(), name="refrigerator_list"),
    path('list/<str:ingredient>/', api.RefrigeratorDetail.as_view(), name="refrigerator_detail"),
]
