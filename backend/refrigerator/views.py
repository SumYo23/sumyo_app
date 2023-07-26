from rest_framework import permissions
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

from django.db import IntegrityError

from .serializers import RefrigeratorCreateSerializer


class RefrigeratorCreateView(generics.CreateAPIView):
    """냉장고 생성"""

    serializer_class = RefrigeratorCreateSerializer
    permission_classes = (permissions.AllowAny,)  # 수정 필요

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(
            data=data,
        )
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        serializer.save(**validated_data)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

