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


class RecipeList2(APIView):
    def post(self, request):
        number = request.data["number"]
        detail = request.data["detail"]
        image_route = request.data["image_route"]
