"""django"""
from django.urls import path

"""local"""
from refrigerator import views

urlpatterns = [
    path('list/', views.RefrigeratorList.as_view(), name="refrigerator_list"), # 냉장고 목록 (GET, POST)
    path('list/<str:ingredient>/', views.RefrigeratorDetail.as_view(), name="refrigerator_detail"), # 냉장고 단일 (PUT, DELETE)
]
