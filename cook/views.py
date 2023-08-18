'''builtin'''
from collections import Counter
import random

'''Third-Party'''
from rest_framework.response import Response
from rest_framework.views import APIView

'''local'''
from user.models import User
from refrigerator.models import Refrigerator
from cook.models import Cook, CookIngredient, CookRecipe, Ingredient
from like.models import Like


# [GET] 0.0.0.0/api/cook/list/
class CookList(APIView):

    def get(self, request, num):
        """사용자별 음식 추천 목록 보여주기"""

        # 변수
        response = Response()
        result = list()

        # 사용자 정보
        user, _ = User.objects.get_or_create(user_number=request.META["HTTP_AUTHORIZATION"])

        # 냉장고 재고
        ingredient = Refrigerator.objects.filter(user=user).values_list("ingredient", flat=True)

        # 냉장고 재고와 겹치는 요리
        cook = Counter(list(CookIngredient.objects.filter(ingredient__in=ingredient).values_list("cook", flat=True)))

        # 요리 보유율
        cook_percent = {
            key: int(value / CookIngredient.objects.filter(cook__pk=int(key)).count() * 100)
            for key, value in cook.items()
        }

        # 요리 보유율 기준 정렬
        cook_percent_sort = sorted(cook_percent.items(), key=lambda x: x[1], reverse=True)

        # 사용자와 안겹치는 요리 목록 (겹치는 요리 목록이 요청한 요리 개수보다 적을 경우 사용)
        cook_no_user = list(set(Cook.objects.all().values_list("pk", flat=True)) - set(cook))

        # 요청받은 요리 수만큼 보여줌
        for i in range(num):
            if len(cook_percent_sort) >= i + 1:
                pk = cook_percent_sort[i][0]
                cook = Cook.objects.get(pk=pk)
                percent = cook_percent_sort[i][1]
                status = "추천"
            else:
                pk = cook_no_user.pop(random.randrange(len(cook_no_user)))
                cook = Cook.objects.get(pk=pk)
                percent = 0
                status = "랜덤"

            # 요리 순서별로 recipes 변수에 저장
            recipes = [
                {
                    "number": recipe.recipe.number,
                    "detail": recipe.recipe.detail,
                    "image_route": recipe.recipe.image_route
                } for recipe in CookRecipe.objects.filter(cook__pk=pk)
            ]

            # 요리 재료 ingredients 변수에 저장
            ingredients = [
                {"name": ingredient.ingredient.name} for ingredient in CookIngredient.objects.filter(cook__pk=pk)
            ]

            # 결과
            result.append(
                {
                    "id": cook.pk,
                    "image_route": cook.image_route,
                    "name": cook.name,
                    "percent": percent,
                    "status": status,
                    "ingredient": cook.ingredient,
                    "recipes": recipes,
                    "ingredients": ingredients

                }
            )

        response.data = result
        return response


class IngredientList(APIView):
    """db 전체 재료(ingredient) 리스트 반환"""

    def get(self, request):
        ingredient_list = list(Ingredient.objects.all().values_list("name", flat=True))
        return Response(ingredient_list)
