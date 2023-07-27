from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Like
from .serializers import LikeSerializer
from .serializers import LikeListSerializer


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
        cook_id = self.kwargs['cook_id']
        like = Like.objects.get(id=cook_id)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LikeListView(generics.ListAPIView):
    serializer_class = LikeListSerializer
    queryset = Like.objects.all()

    def list(self, request, *args, **kwargs):
        if self.request.query_params.get('page', None) is None:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(
                queryset,
                many=True,
            )
            return Response(serializer.data)
        return super().list(request, *args, **kwargs)
