'''buit-in'''
from collections import Counter
import random

'''Third-party'''
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView

'''local'''
from cook.models import CookIngredient, Cook
from refrigerator.models import Refrigerator
from user.models import User
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
        like_id = self.kwargs['like_id']
        like = Like.objects.get(id=like_id)
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LikeListView(generics.ListAPIView):
    serializer_class = LikeListSerializer
    queryset = Like.objects.all()


class LikeList(APIView):
    def get(self, request):

        # user_number = abcd1234
        user, _ = User.objects.get_or_create(user_number=request.META["HTTP_AUTHORIZATION"])
        if Like.objects.filter(user=user.id).exists():
            likes = Like.objects.filter(user=user.id)

            result = list()
            for like in likes:
                cook = like.cook
                recipes = [
                    {
                        "number": recipe.number,
                        "detail": recipe.detail,
                        "image_route": recipe.image_route
                    } for recipe in cook.cook_recipe.all()
                ]

                ingredients = [
                    {"name": ingredient.name} for ingredient in cook.cook_ingredient.all()
                ]

                result.append(
                    {
                        "id": cook.pk,
                        "image_route": cook.image_route,
                        "name": cook.name,
                        "is_like": True,
                        "ingredient": cook.ingredient.replace('주재료', '').split(','),
                        "recipes": recipes,
                        "ingredients": ingredients

                    }
                )

            response = Response()
            response.data = result
            return response
        return Response('찜목록이 없습니다.')
