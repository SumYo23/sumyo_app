'''builtin'''
from collections import Counter

'''Third-Party'''
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

'''Django'''
from user.models import User
from refrigerator.models import Refrigerator
from cook.models import Cook, CookIngredient


# 사용자별 음식 추천 목록 보여주기
class CookList(APIView):
    def get(self, request, num):
        ## 사용자 정보 ##
        user, _ = User.objects.get_or_create(user_number=request.META["HTTP_AUTHORIZATION"])

        ## 사용자 냉장고 재고 ##
        user_ingredient = Refrigerator.objects.filter(user=user).values_list("ingredient", flat=True)

        ## 사용자 냉장고 재고와 겹치는 요리들 ##
        user_cook = CookIngredient.objects.filter(ingredient__in=user_ingredient).values_list("cook", flat=True)
        counter = Counter(list(user_cook))
        print(counter)

        return Response({"message": "success"})
