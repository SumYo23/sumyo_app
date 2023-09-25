'''Third-party'''
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView

'''local'''
from user.models import User
from .models import Like
from cook.models import Cook
from .serializers import LikeSerializer
from .serializers import LikeListSerializer


class LikeList(APIView):

    def get(self, request):
        """사용자별 음식 찜 목록 보여주기"""

        # 변수
        result = list()
        response = Response()

        # 사용자 정보
        user, _ = User.objects.get_or_create(user_number=request.META["HTTP_AUTHORIZATION"])  # user_number = abcd1234

        # 사용자 좋아요 정보
        if Like.objects.filter(user=user.id).exists():
            likes = Like.objects.filter(user=user.id)

            for like in likes:
                # 찜한 요리 1개
                cook = like.cook

                # 요리 레시피 리스트
                recipes = [
                    {
                        "number": recipe.number,
                        "detail": recipe.detail,
                        "image_route": recipe.image_route
                    } for recipe in cook.cook_recipe.all()
                ]

                # 요리 재료 리스트
                ingredients = [
                    {"name": ingredient.name} for ingredient in cook.cook_ingredient.all()
                ]

                # 찜 목록
                result.append(
                    {
                        "id": cook.pk,
                        "image_route": cook.image_route,
                        "name": cook.name,
                        "percent": 0,
                        "is_like": True,
                        "ingredient": cook.ingredient,
                        "recipes": recipes,
                        "ingredients": ingredients

                    }
                )

            response.data = result
            return response
        else:
            response.data = []
            return Response(result)


class LikeDetail(APIView):
    """찜 상태 변경"""

    def post(self, request):
        """찜 하기"""
        user, _ = User.objects.get_or_create(user_number=request.META["HTTP_AUTHORIZATION"])
        cook = Cook.objects.get(pk=request.data["cook_id"])
        Like.objects.get_or_create(cook=cook, user=user)
        return Response({"message": "success"})

    def delete(self, request):
        """찜 안하기"""
        user, _ = User.objects.get_or_create(user_number=request.META["HTTP_AUTHORIZATION"])
        cook = Cook.objects.get(pk=request.data["cook_id"])
        Like.objects.filter(cook=cook, user=user).delete()
        return Response({"message": "success"})
