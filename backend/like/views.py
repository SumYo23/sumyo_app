from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Like
from .serializers import LikeSerializer


class LikeCreateView(generics.CreateAPIView):
    serializer_class = LikeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        Like.objects.create(**validated_data)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


class LikeDestroyView(generics.DestroyAPIView):
    serializer_class = LikeSerializer

    def destroy(self, request, *args, **kwargs):
        like_id = self.kwargs['like_id']
        like = Like.objects.get(id=like_id)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
