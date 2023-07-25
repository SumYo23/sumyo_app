from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cook.serializers import RecipeSerializer


class RecipeList(APIView):
    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeList2(APIView):
    def post(self, request):
        number = request.data["number"]
        detail = request.data["detail"]
        image_route = request.data["image_route"]
