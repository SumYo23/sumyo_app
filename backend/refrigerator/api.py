"""Third-party"""
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

"""local"""
from cook.models import Ingredient
from refrigerator.models import Refrigerator
from user.models import User


# [GET || POST] 0.0.0.0/api/refrigerator/list/
class RefrigeratorList(APIView):
    def get(self, request):
        """
            냉장고 재고 목록
            [GET] Header = {"Authorization" : 기기고유번호 }
        """
        user, _ = User.objects.get_or_create(user_number=request.META["HTTP_AUTHORIZATION"])
        refrigerator = Refrigerator.objects.filter(user__pk=user.pk)

        response = Response()
        response.data = list()
        for refr in refrigerator:
            response.data.append(
                {"ingredient": refr.ingredient.name, "quantity": refr.quantity, "date": refr.add_date})
        response.status = status.HTTP_200_OK
        return response

    def post(self, request):
        """
            냉장고 재고 추가
            [POST] Header = {"Authorization" : 기기고유번호 }
            {
                "ingredient" : "사과",
                "quantity" : 5
            }
        """

        # 요청 데이터 받기
        user, _ = User.objects.get_or_create(user_number=request.META["HTTP_AUTHORIZATION"])
        ingredient = request.data["ingredient"]
        quantity = request.data["quantity"]

        # 재료와 수량 추가(필드가 없으면 생성)
        ingredient_instance, _ = Ingredient.objects.get_or_create(name=ingredient)
        refrigerator_instance, _ = Refrigerator.objects.get_or_create(ingredient=ingredient_instance, user=user)
        refrigerator_instance.quantity = int(refrigerator_instance.quantity) + int(quantity)  # 입력한 만큼 더해지도록
        refrigerator_instance.save()

        # Response
        response = Response()
        response.data = {
            "ingredient": refrigerator_instance.ingredient.name,
            "quantity": int(refrigerator_instance.quantity),
            "date": refrigerator_instance.add_date
        }
        response.status = status.HTTP_200_OK
        return response


# [PUT || DELETE] 0.0.0.0/api/refrigerator/list/<str:ingredient>
class RefrigeratorDetail(APIView):
    def put(self, request, ingredient):
        """
            냉장고 재고 수정
            [PUT] Header = {"Authorization" : 기기고유번호 }
            {
                "ingredient" : "사과",
                "quantity" : 5
            }
        """

        # 요청 데이터 받기
        user, _ = User.objects.get_or_create(user_number=request.META["HTTP_AUTHORIZATION"])
        quantity = request.data["quantity"]

        # 재료를 기준으로 수량 변경
        ingredient_instance = Ingredient.objects.get(name=ingredient)
        refrigerator_instance = Refrigerator.objects.get(ingredient=ingredient_instance, user=user)
        refrigerator_instance.quantity = quantity
        refrigerator_instance.save()

        # Response
        response = Response()
        response.data = {
            "ingredient": refrigerator_instance.ingredient.name,
            "quantity": int(quantity),
            "date": refrigerator_instance.add_date
        }
        return response

    def delete(self, request, ingredient):
        """
            냉장고 재고 삭제
        """

        # 요청 데이터 받기
        user, _ = User.objects.get_or_create(user_number=request.META["HTTP_AUTHORIZATION"])

        # ingredient를 기준으로 재료 삭제
        ingredient_instance = Ingredient.objects.get(name=ingredient)
        refrigerator_instance = Refrigerator.objects.get(ingredient=ingredient_instance, user=user)
        refrigerator_instance.delete()
        return Response(status=status.HTTP_200_OK)
