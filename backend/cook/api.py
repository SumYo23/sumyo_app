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

        ## 냉장고 재고 ##
        user_ingredient = Refrigerator.objects.filter(user=user).values_list("ingredient", flat=True)

        ## 냉장고 재고와 겹치는 요리들 일치율 순서로 정렬 ##
        user_cook = CookIngredient.objects.filter(ingredient__in=user_ingredient).values_list("cook", flat=True)
        user_cook_cnt = Counter(list(user_cook))
        user_cook_cnt = sorted(user_cook_cnt.items(), key=lambda x: x[1], reverse=True)  # 겹치는 개수 순서로 정렬
        user_cook_list = [u[0] for u in user_cook_cnt]

        result = list()
        ## 요청받은 수만큼 정렬
        if len(user_cook_list) > num:
            for i in range(num):
                cook = Cook.objects.get(pk=user_cook_list[i])
                result.append(
                    {
                        "id": cook.pk,
                        "image_route": cook.image_route,
                        "name": cook.name,
                        "percent": 100
                    }
                )
        else:
            pass

        response = Response()
        response.data = result
        response.status = status.HTTP_200_OK
        return response
