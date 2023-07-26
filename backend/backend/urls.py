"""django"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),  # 어드민 페이지
    path("backoffice/", include("backoffice.urls")),  # 백오피스(데이터 입력할 때 사용)
    path("api/refrigerator/", include("refrigerator.urls")),  # refirigerator app
    path("api/cook/", include("cook.urls")),  # cook app
    path("api/like/", include("like.urls")),  # like app
]
