'''Built-in'''
import shutil

'''Third-Party'''
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

'''Local'''
from ai.classifier import predict
from ai.models import Image
from ai.serializers import ImageSerializer


class ImageDetaction(APIView):
    def post(self, request):
        serializer = ImageSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            image_route = serializer.data.get("image")
            result = {"foods": predict(image_route)}

            shutil.rmtree("./images")
            Image.objects.all().delete()

            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
