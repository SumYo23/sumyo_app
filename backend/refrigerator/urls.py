from django.urls import path

from refrigerator import api

urlpatterns = [
    path('list/', api.RefrigeratorList.as_view(), name="refrigerator_list"),
    path('list/<str:ingredient>/<int:quantity>/', api.RefrigeratorPut.as_view(), name="refrigerator_put"),
    path('list/<str:ingredient>/', api.RefrigeratorDelete.as_view(), name="refrigerator_delete"),
]
